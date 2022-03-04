import json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://www.latlong.net/category/airports-236-19.html"
html = urllib.request.urlopen(url).read()
#print(html.decode())
soup = BeautifulSoup(html, "html.parser")

#retrive contents of table
s=soup.find('table')
tags=s('td')
count=0
data=[]

#form a list of contents in json format
item=[]
for tag in tags:
    if tag.find('a') is None:item.append(tag.text)
    else:item.append(tag.find('a').get('title',None))
    count=count+1
    if count%3==0:
        d={
        "placeName":str(item[0]),
        "latitude":str(item[1]),
        "longitude":str(item[2])
        }
        data.append(d)
        item=[]
data=json.dumps(data,indent = 4)
print(data)
