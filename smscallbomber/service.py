import random
import string
import requests
import re
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

    @staticmethod
    def fetch_proxies(url):
        try:
            res = requests.get(url, timeout=3)
            res.raise_for_status()
            lines = res.text.splitlines()
            proxies = [line.strip() for line in lines if re.match(r'^\d+\.\d+\.\d+\.\d+:\d+$', line.strip())]
            
            return proxies
        except requests.RequestException:
            return []

    @staticmethod
    def check_proxy(proxy):
        try:
            res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy}, timeout=3)
            return res.status_code == 200
        except requests.RequestException:
            return False

    def generate_proxy(self):
        proxy_sources = [
            "https://api.openproxylist.xyz/http.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://www.sslproxies.org/",
            "https://www.proxy-list.download/api/v1/get?type=https",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            'https://www.sslproxies.org/',
            'https://www.google-proxy.net/',
            'https://free-proxy-list.net/anonymous-proxy.html',
            'https://free-proxy-list.net/uk-proxy.html',
            'https://www.us-proxy.org/',
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all',
            'https://free-proxy-list.net/'
        ]

        random.shuffle(proxy_sources)

        for url in proxy_sources:
            proxies = self.fetch_proxies(url)
            random.shuffle(proxies)

            for proxy in proxies:
                if self.check_proxy(proxy):
                    return {"http": proxy, "https": proxy}
                else:
                    break

        return None

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