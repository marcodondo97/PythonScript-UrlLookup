#!/usr/bin/env python3
import socket
import requests
from urllib.parse import urlparse
import whois
import webtech
import os
import sys


print(r"""
--------------------------------------------------
 _   _      _   _             _                
| | | |    | | | |           | |               
| | | |_ __| | | | ___   ___ | | ___   _ _ __  
| | | | '__| | | |/ _ \ / _ \| |/ / | | | '_ \ 
| |_| | |  | | | | (_) | (_) |   <| |_| | |_) |
 \___/|_|  |_| |_|\___/ \___/|_|\_\\__,_| .__/ 
                                        | |    
                                        |_|    
--------------------------------------------------
Author: Marco Dondo  https://github.com/marcodondo97
Version: 1.0
--------------------------------------------------
""")


wt = webtech.WebTech(options={'json': True})

#pip install requests
#pip install python-whois
#pip install webtech

dir=os.getcwd()



line = (sys.argv[1])
request = requests.get(line)
if request.status_code == 200 or 301 or 302:
    print()
    print("Checking: "+ line)
    print('Web site exists and it is up')
    domain=(urlparse(line).netloc)
    url= "http://"+domain
    ip_address= (socket.gethostbyname(domain.strip()))
    print("Nslookup: "+ ip_address)
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    print("Location:",response.get("city"),"-",response.get("country_name"))
    r = requests.get(line)
    print("Redirect to: " +r.url)
    whois_info = whois.whois(domain)
    print("Domain registrar:", whois_info.registrar)
    print("Creation date:", whois_info.creation_date)
    print("Expiration date:",whois_info.expiration_date)
    print("WHOIS server:", whois_info.whois_server)
    if ((requests.get(url +"/wp-login.php")).status_code) == 200:
        print("CMS: Wordpress")
    elif ((requests.get(url+"/administrator")).status_code) == 200:
        print("CMS: Joomla")
    elif ((requests.get(url+"/user/login")).status_code)== 200:
        print("CMS: Drupal")
    else: 
        print("CMS not found")
            
    report = (wt.start_from_url(url))
    print("More information about technologies used: ",report['tech'])
            
else:
    print('Web site does not exist or is down')
        



"""
Introducion

Python script to scan URL, get informtion about domain and website's technologies/languages.

Description

This python script can be used for scan any URL and get the following infromation:

-HTTP response
-Nslookup IP
-IP location
-Redirect destination
-Domain registrar 
-Domain creation and expiration date
-Domain manager
-CMS used
-Information about technologies/languages used

The domains to scan have to be written inside the Domains.txt file and the script will read the url's lines.

Before starting make sure you install the following packages:

pip install requests
pip install python-whois
pip install webtech
"""