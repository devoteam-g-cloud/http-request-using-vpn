# HTTP request using a VPN

I had to make an API call to an endpoint protected by a VPN. When looking for documentation, I mainly found posts about issues making an API call rather than how to do it.

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


