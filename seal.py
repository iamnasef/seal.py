import requests
import os
import urllib
import time

year = 2020
for i in range(1,13):
    for j in range (1,32):
            base="http://dc.intelligence.htb/documents/"
            name=str(year)+"-"+str(i).zfill(2)+"-"+str(j).zfill(2)+"-upload.pdf"
            url=base+name
            r=requests.get(url)
            if r.status_code!=404:
                print("[+]Downloading : "+url)
                os.system("wget -q "+url)
for i in os.listdir("."):
    os.system("exiftool "+i+" | grep Creator | cut -c 35- >>wordlist") 
