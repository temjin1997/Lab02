import requests
import json
from pprint import pprint

router = {"ip": "10.50.50.20", "port": "443",
          "user": "cisco", "password": "cisco"}

headers = {"Accept": "application/yang-data+json",
           "Content-type": "pplication/yang-data+json"}

url = f"https://{router['ip']}:{router['port']}/api/mo/sys/intf/phys-[eth1/3].json?subscription=yes&query-target=subtree"
print(url)

