# Hack urls

import re
import requests
import sys
from pyfiglet import Figlet
from termcolor  import colored


f = Figlet(font="standard")
print(colored(f.renderText("HackUrls"),"green"))

def get_urls():
    url = requests.get(sys.argv[1])
    txt = url.text
    regex ="https?://(?:[-\w.]|(?:%[\da-fA-F]{1}))+"
    urls=re.findall(regex,txt)
    print(colored("200 Status Urls",'red'))
    for url in urls:
        status = requests.get(url)
        if status.status_code ==200:
              print(url)
        elif status.status_code == 404:
              print(colored("404 Status Urls",'blue'))
              print(url)
        elif status.status_code == 403:
              print(colored("403 Status Urls","cyan"))
              print(url)

if len(sys.argv)!= 1 and len(sys.argv)!=3:
     get_urls() 
else:
    print("Error,Only Single Url accpet,Please Enter url")
     
