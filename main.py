import requests
from requests.auth import HTTPProxyAuth

user = "" # username used when logging to your VPN
password = "" # password used when logging to your VPN
proxy_address = "" # proxy ip address
proxy_port = "" # proxy port (I mainly used 8080)
token = "" # if your API also required auth
url_to_call = "" # the url of the endpoint you want to call

proxy_string = f'http://{user}:{password}@{proxy_address}:{proxy_port}'

s = requests.Session()
s.proxies = {"http": proxy_string, "https": proxy_string}
s.auth = HTTPProxyAuth(user, password)
s.trust_env = False
r = s.get(
    url_to_call,
    proxies={"http": proxy_string, "https": proxy_string},
    headers={
        "Authorization": f"Bearer {token}"
    }
)
print()
