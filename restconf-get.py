import requests
import json
from pprint import pprint

router = {"ip": "10.50.50.20", "port": "443",
          "user": "cisco", "password": "cisco"}

# set REST API headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"
# print(url)

response = requests.get(url, headers=headers, auth=(router['user'], router['password']), verify=False)


api_data = response.json()



print(api_data)
print("/" * 50)
print(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print("/" * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
    print('Interface is up')