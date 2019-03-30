import json
import requests

api_url_base = 'https://api.lyrics.ovh/v1/'
headers = {'Content-Type': 'application/json',
           'charset': 'utf-8'}

def get_lyrics_info():

    api_url ='{0}Dance%20Gavin%20Dance/Awkward'.format(api_url_base)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

lyric_info = get_lyrics_info()

if lyric_info is not None:
    print("Here is your info: ")
    for lyrin in lyric_info["lyrics"].split('\n'):
       print(lyrin)

else:
    print('[!] Request Failed')
