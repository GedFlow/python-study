import socket
import requests
import re

inAddr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inAddr.connect(("www.google.co.kr", 443))
print("내부 IP: ", inAddr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
outAddr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ", outAddr)