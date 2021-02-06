import requests
from pprint import pprint

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://10.50.50.19:443/api/aaaLogin.json"

payload="{\r\n\"aaaUser\":{\r\n\"attributes\":{\r\n\"name\":\"cisco\",\r\n\"pwd\":\"cisco\"\r\n}\r\n}\r\n}"


headers = {
  'Content-Type': 'application/json',
#  'Authorization': 'Basic Y2lzY286Y2lzY28=',
#  'Cookie': 'APIC-cookie=Bafb0YYMUqG6S3t+TRXXBkdjDfwCQR7XiKC3Us81l9jCzQg8i1IFwDeo1eysZoqFqqSISLc1mymtIElYcps4JxPrEu1NEXVFEsH8iGqAQ2J674FHyiJrLoPz1kVdix6tBVfw//mABJfXVQkBF9gxCbdvsKuoEZlTLO3Q/fsawFU=; nxapi_auth=fewhg:uM2er2s99LjTWTErAkB5BzGTKCg='
}

response = requests.post(url, headers=headers, verify=False, data=payload).json()
print ('#' * 20 +" Login response" + '#' * 20 )
pprint(response)


token = response['imdata'][0]['aaaLogin']['attributes']['token']
print ('#' * 20 +" token " + '#' * 20 )
print(token)

cookies = {}
cookies['APIC-cookie']=token


url = "https://10.50.50.19:443/api/node/mo/sys/intf/phys-[eth1/1].json"

# get interfaces decsription
payload={}
get_response = requests.get(url, headers=headers, data=payload, cookies=cookies, verify=False ).json()
print ('#' * 20 +" get interface information " + '#' * 20 )
int_desc = get_response['imdata'][0]['l1PhysIf']['attributes']['descr']
pprint(int_desc)


# update interfaces decsription
payload="\r\n{\r\n\"l1PhysIf\": {\r\n \"attributes\": {\r\n\r\n\"descr\":\"new script\",\r\n\r\n}\r\n}\r\n}\r\n"
headers = {
  'Content-Type': 'application/json',
#  'Authorization': 'Basic Y2lzY286Y2lzY28=',
  
}
put_response = requests.put(url, headers=headers, data=payload, cookies=cookies, verify=False ).json()
print ('#' * 20 +" update interface information " + '#' * 20 )
pprint(put_response)

# get interfaces decsription
payload={}
get_response = requests.get(url, headers=headers, data=payload, cookies=cookies, verify=False ).json()
print ('#' * 20 +" get interface information " + '#' * 20 )
int_desc = get_response['imdata'][0]['l1PhysIf']['attributes']['descr']
pprint(int_desc)
