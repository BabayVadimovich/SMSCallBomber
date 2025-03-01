import random
import string
import requests
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
        self.proxy = None
        if proxy:
            self.proxy = proxy if proxy is not True else self.generate_proxy()
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

    def generate_proxy(self):
        proxy = requests.get("https://gimmeproxy.com/api/getProxy?curl=true&get=true&cookies=true&referer=true&user-agent=true&minSpeed=50&post=true&protocol=http&supportsHttps=true&maxCheckPeriod=3600")
        return {"http": proxy.text, "https": proxy.text}

    def get_domain_name(self):
        website = self.service_info['info'].get('website', '')
        if website:
            return website
        return ''

    def send_request(self):
        self.__parse_data()
        self.__replace_data()

        session = requests.Session()
        request = requests.Request(self.method.upper(), self.url, headers=self.headers, cookies=self.cookies, data=self.data, json=self.json)
        request = request.prepare()
        if self.proxy:
            session.proxies = self.proxy
        response = session.send(request, timeout=self.timeout)
        return response.status_code