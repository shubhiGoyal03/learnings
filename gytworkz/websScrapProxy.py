import requests
import random
from bs4 import BeautifulSoup as bs
import traceback
#get proxies
def get_free_proxies():
    url="https://free-proxy-list.net/"
    data=requests.get(url).content
    #print(data)
    soup=bs(data,'html.parser').find('table')
    proxies=[]
    tags=soup('tr')
    for i in tags[1:]:
        proxies.append(i.contents[0].text+":"+i.contents[1].text)
    return proxies

proxies=get_free_proxies()
url="http://httpbin.org/ip"
for i in (proxies):
    print("---------------------------")
    try:
        print(requests.get(url,proxies={"http":i,"https":i},timeout=2).json())
    except:pass
