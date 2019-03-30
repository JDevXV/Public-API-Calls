
import requests
import json
import urllib.request

cardid = input("What is the id?: ")
card_request = """https://api.magicthegathering.io/v1/cards.json?id=%s""" % cardid

response = requests.get(card_request)
data = response.json()
cardinfo = data["cards"]

for item in cardinfo:
  print(item["name"] + " - " + item["type"] + " - " + item["rarity"] + " - " + str(item["colors"]))





