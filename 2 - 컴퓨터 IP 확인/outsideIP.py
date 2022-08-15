import requests
import re

req = requests.get("http://ipconfig.kr")
outAddr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(outAddr)