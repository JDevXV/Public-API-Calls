import json
import requests

api_url_base = 'http://www.boredapi.com/api/activity'
headers = {'Content-Type': 'application/json',
           'charset': 'utf-8'}

def get_activity():
    response = requests.get(api_url_base, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

activity = get_activity()

if activity is not None:
    print("""Here is your activity:
    """)
    for act in activity["activity"].split('\n'):
       print(act)
    for type in activity["type"].split('\n'):
       print("Type:",type)
    for part in str(activity["participants"]):
       print("Participants:",part)
    for price in str(activity["price"]).split('\n'):
       print("Price:",price)

else:
    print('[!] Request Failed')

