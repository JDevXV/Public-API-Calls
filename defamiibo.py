import json
import requests

api_url_base = 'http://www.amiiboapi.com/api/amiibo/'
headers = {'Content-Type': 'applicaton/json'}

def get_amiibo_info():

    api_url = '{0}?'.format(api_url_base)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

amiibo_info = get_amiibo_info()

if amiibo_info is not None:
    print("Here's your info: ")
    for amin in amiibo_info['amiibo']:
        print('{0}'.format(amin))

else:
    print('[!] Request Failed')

