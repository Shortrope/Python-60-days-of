import json
import requests

api_url_base = 'https://shazam.antsle.us/api/'

def get_login_token():
    creds = {"username": "mak", "password": "hellodolly"}
    loginheaders = {"Content-Type": "application/json"}
    api_url = '{0}login'.format(api_url_base)
    response = requests.post(api_url, headers=loginheaders, json=creds)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))["token"]
    else:
        return None

api_token = get_login_token()
getheaders = {"Authorization": "Token {0}".format(api_token)}


def get_antlets():
    api_url = '{0}antlets'.format(api_url_base)
    response = requests.get(api_url, headers=getheaders)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_antlet(name):
    api_url = '{0}antlets/{1}'.format(api_url_base, name)
    response = requests.get(api_url, headers=getheaders)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

antlets_info = get_antlets()

if antlets_info is not None:
    print("Shazam's Antlets: ")
    print("antlets_info Data type: {0}".format(type(antlets_info)))
    antlet_names = []
    for ant in antlets_info:
        antlet_names.append(ant["dname"])
    antlet_names.sort()
    for name in antlet_names:
        print(name)
else:
    print('[!] Request Failed')
