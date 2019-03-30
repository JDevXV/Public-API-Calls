import requests
import json
import urllib.request

response = requests.get("http://www.amiiboapi.com/api/amiibo/?name-isabelle.json
data = response.json()
characterlist = data['amiibo']

for item in characterlist:
  print(item["amiiboSeries"] + " - " + item["character"])