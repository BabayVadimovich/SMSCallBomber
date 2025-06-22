import random
import string
import aiohttp
import smscallbomber.config as cfg

def username():
    names = cfg.names
    return random.choice(names)

def email():
    emails = cfg.emails
    return username() + randomNums() + random.choice(emails)

def randomPass():
    return username() + randomNums()

def randomNums():
    ls = [str(random.randint(10, 99)) for i in range(2)]
    return "".join(ls)

def randomToken():
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for i in range(30))


class Service:
    def __init__(self, service_info, phone, timeout, proxy):
        self.service_info = service_info
        self.timeout = timeout
        self.proxy = proxy
        self.phone = phone

    def __parse_data(self):
        self.method = self.service_info['method']
        self.url = self.service_info['url']
        self.headers = self.service_info.get('headers', {})
        self.cookies = self.service_info.get('cookies', {})
        self.data = self.service_info.get('data', {})
        self.json = self.service_info.get('json', {})


    def __replace_data(self):
        for old, new in {
            "%phone%": self.phone,
            "%name%": username(),
            "%email%": email(),
            "%password%": randomPass(),
            "%token%": randomToken()
        }.items():
            if old in str(self.data):
                self.data = str(self.data).replace(old, new)
            if old in str(self.json):
                self.json = str(self.json).replace(old, new)

    def get_domain_name(self):
        website = self.service_info['info'].get('website', '')
        if website:
            return website
        return ''

    async def send_request(self, session):
        self.__parse_data()
        self.__replace_data()
        request_kwargs = {
            "method": self.method.upper(),
            "url": self.url,
            "headers": self.headers,
            "cookies": {k: v for k, v in self.cookies.items() if k not in {"Secure", "HttpOnly", "SameSite"}},
            "proxy": self.proxy if isinstance(self.proxy, str) else None
        }
        if self.json is not None:
            request_kwargs["json"] = self.json
        elif self.data is not None:
            request_kwargs["data"] = self.data
        async with session.request(**request_kwargs) as response:
            return response.status