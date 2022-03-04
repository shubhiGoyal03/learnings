import json
import requests
import urllib.request, urllib.parse, urllib.error
place=input("Enter city: ")
url="http://api.openweathermap.org/data/2.5/weather?"
param={"q": place , "appid":"4f3bd979ed8d7e8c58e7fc988ff8c06b","units":"metric"}
url=url+urllib.parse.urlencode(param)
print(url)
uh=urllib.request.urlopen(url)
data=uh.read().decode()
d=json.loads(data)
#print(d["list"])
#print(json.dumps(d,indent=4))
#for v in d["list"]:
#    print(v.get("dt_txt"))
print(d)
