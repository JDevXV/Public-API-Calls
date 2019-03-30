import requests
import json
import urllib.request

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
peoplelist = data['people']

for item in peoplelist:
    print(item['name'] + " - " + item['craft'])



print("""


""")



print((data['people'][0]['name']) + (" - ") + (data['people'][0]['craft']))
print((data['people'][1]['name']) + (" - ") + (data['people'][1]['craft']))
print((data['people'][2]['name']) + (" - ") + (data['people'][2]['craft']))