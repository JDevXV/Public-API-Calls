
import requests
import json
import urllib.request

artistname = input("What is the artist name?: ").replace(' ', '%20')
songname = input("What is the title of the song?: ").replace(' ', '%20')

lyricrequest = """https://api.lyrics.ovh/v1/%s/%s""" % (artistname,songname)

response = requests.get(lyricrequest)
data = response.json()
lyrics = data["lyrics"]

print(lyrics)
