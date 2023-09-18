

import os
try:
    import requests;from requests import *
except:
    try:
        os.system("pip install requests")
        import requests;from requests import *
    except:
        print("installation error! - python3 requests")

import json
import socket
import threading
import concurrent.futures
import os
import sys
import time
import random
import subprocess
import platform


ip = input("\n<IP&4>: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
print_lock = threading.Lock()
response = requests.get(f'http://ip-api.com/json/{ip}').content
data = json.loads(response)

try:
    print(f"""
[+]IP: {data['query']}
[+]Country: {data['country']}
[+]Region: {data['regionName']}
[+]City: {data['city']}
[+]Zip: {data['zip']}
[+]Latitude: {data['lat']}
[+]Longitude: {data['lon']}
[+]ISP: {data['isp']}
[+]ICMP reply: {data ['status']}""")


except:
    print("\n[!]This ip seems to be invalid.")
    exit()

response = requests.get("https://vpnapi.io/api/" + ip + "?key=ca7522e3d80a4e308945e0ca3c979d6c")
data = json.loads(response.text)



if data["security"]["vpn"] == False:
	pass
else:
	print("[!]Possible VPN or Traffic Hosting service Detected")


if data["security"]["proxy"] == False:
    pass
else:
    print("[!]Proxy Server Detected")

if data["security"]["tor"] == False:
    pass
else:
    print("[!]Tor Anonymity Service Detected")

response = requests.get(f'http://ip-api.com/json/{ip}').content
data = json.loads(response)
string = f'''{data['isp']}'''
string = str(string)

if "Cloudflare, Inc." in string:
    print("[!]Cloudflare Service Detected")
    pass

response = requests.get(f'http://ip-api.com/json/{ip}').content
data = json.loads(response)
string = f'''{data['isp']}'''
string = str(string)

if "OVH" in string:
    print("[!]Possible OVH Detected")
else:
    pass

response = requests.get(f'http://ip-api.com/json/{ip}').content
data = json.loads(response)
string = f'''{data['isp']}'''
string = str(string)

if "Google" in string:
    print("[!]Possible Google service Detected")
else:
    pass

response = requests.get(f'http://ip-api.com/json/{ip}').content
data = json.loads(response)
string = f'''{data['isp']}'''
string = str(string)

if "Amazon" in string:
    print("[!]Possible Amazon service Detected")
else:
    pass

response = requests.get(f'http://ip-api.com/json/{ip}').content
data = json.loads(response)
string = f'''{data['isp']}'''
string = str(string)

if "Facebook" in string:
    print("[!]Possible Facebook service Detected")
else:
    pass

response = requests.get(f'http://ip-api.com/json/{ip}').content
data = json.loads(response)
string = f'''{data['isp']}'''
string = str(string)

if "Microsoft" in string:
    print("[!]Possible Microsoft service Detected")
else:
    pass


host = ip
ip = socket.gethostbyname(host)
response = requests.get(f'http://ip-api.com/json/{ip}').content
data = json.loads(response)
cunt = data['country']
headers = {
    "Range": "bytes=0-%s" % "".join(
        [",5-%s" % x for x in range(1,1301)]
        ),
    "Accept-Encoding": "gzip",
    "Connection": "close",
    }

try:
    host = 'http://'+host
    h = httplib2.Http()
    resp, cont = h.request(host, "HEAD", headers=headers)
    print("[Web-Server]",resp["server"])

except:
    
    pass




time.sleep(10)
