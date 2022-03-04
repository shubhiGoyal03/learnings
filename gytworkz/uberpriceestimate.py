import json
import requests
from bs4 import BeautifulSoup

url = "https://www.uber.com/api/loadFEEstimates?localeCode=en"
headers = {"authority":"www.uber.com",
"method":"POST",
"Cookie":"marketing_vistor_id=70c767da-bf06-4ada-8217-7297a3171bd6",
"path":"/api/loadFEEstimates?localeCode=en",
"scheme": "https",
"accept-encoding": "gzip, deflate, br",
"sec-ch-ua":"""Not;A Brand";"v"="99", "Google Chrome";"v"="97", "Chromium";"v"="97" """,
"content-length": "291",
"content-type":"application/json",
"x-csrf-token":"x",
"sec-ch-ua-mobile":"?0",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
"sec-ch-ua-platform":"Windows",
"accept":"*/*",
"origin":"https://www.uber.com",
"sec-fetch-site":"same-origin",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://www.uber.com/global/en/price-estimate/",
"accept-language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
"cookie": """_ua={"session_id":"5981be9f-27ef-48b6-9075-f3674e075e81","session_time_ms":1642664879269}; marketing_vistor_id=70c767da-bf06-4ada-8217-7297a3171bd6; uber_sites_geolocalization={%22best%22:{%22localeCode%22:%22en%22%2C%22countryCode%22:%22GLOBAL%22%2C%22territoryId%22:474%2C%22territorySlug%22:%22jaipur%22%2C%22territoryName%22:%22Jaipur%22}%2C%22url%22:{%22localeCode%22:%22en%22%2C%22countryCode%22:%22GLOBAL%22}%2C%22user%22:{%22countryCode%22:%22IN%22%2C%22territoryId%22:474%2C%22territoryGeoJson%22:[[{%22lat%22:30.1950493%2C%22lng%22:72.7897034}%2C{%22lat%22:30.1950493%2C%22lng%22:78.2622375}%2C{%22lat%22:25.6811409%2C%22lng%22:78.2622375}%2C{%22lat%22:25.6811409%2C%22lng%22:72.7897034}]]%2C%22territoryGeoPoint%22:{%22latitude%22:26.9124%2C%22longitude%22:75.7873}%2C%22territorySlug%22:%22jaipur%22%2C%22territoryName%22:%22Jaipur%22%2C%22localeCode%22:%22en%22}}; optimizelyEndUserId=oeu1642664876829r0.149592329372227; segmentCookie=b; utag_geo_code=IN; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NDI2NjQ4ODAsImV4cCI6MTY0Mjc1MTI4MH0.N3zE-J39sgEDHSt48sZ2V0UlKJxcCETLx0no8WJzUeA; UBER_CONSENTMGR=1642664878603|consent:true; CONSENTMGR=1642664878603:undefined%7Cconsent:true%7Cc1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1642664878605; _gcl_au=1.1.7697559.1642664879; _ga=GA1.2.1479589290.1642664881; _gid=GA1.2.1386107672.1642664881; utag_main=v_id:017e7674dd7300307b74c5fbe58005072002e06a00978$_sn:1$_ss:0$_st:1642667692671$ses_id:1642664877432%3Bexp-session$_pn:4%3Bexp-session$segment:a$optimizely_segment:a"""
}
data = {"origin":{"id":"ChIJE_whhgu0bTkRCdE1GKpE8Zc","provider":"google_places","locale":"en","latitude":26.9098861,"longitude":75.7830211},"destination":{"id":"ChIJGXfwUfizbTkRIcHXzAUkPMA","provider":"google_places","locale":"en","latitude":26.8289443,"longitude":75.8056178},"locale":"en"}

response = requests.post(url, headers=headers, json=data)
r=response.text
j=json.loads(r)
for i in j["data"]["prices"]:
    print(i["vehicleViewDisplayName"]," : ",i["fareString"])
