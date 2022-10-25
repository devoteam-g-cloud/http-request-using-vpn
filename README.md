# HTTP request using a VPN

The objective of this snippet is to provide people with a solution to make HTTP requests when the server you are trying to contact is only available via VPN.

## Setup

### Project

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Variables 

There are multiple variables to setup
```
user = "" # username used when logging to your VPN
password = "" # password used when logging to your VPN
proxy_address = "" # proxy ip address
proxy_port = "" # proxy port (I mainly used 8080)
token = "" # if your API also required auth
url_to_call = "" # the url of the endpoint you want to call
```


