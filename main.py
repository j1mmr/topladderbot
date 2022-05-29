import os
import time

from dotenv import load_dotenv, find_dotenv

#requires pip package python-find_dotenv

import urllib.request
import json

load_dotenv(find_dotenv())

cr_key = os.getenv('crKey')
base_url = "https://api.clashroyale.com/v1/locations/"
endpoint = "/rankings/players?limit=1"
trophies = 0

while 1==1:
    loc = 57000007
    while loc <= 57000260:
        request = urllib.request.Request(
        base_url+str(loc)+endpoint,
        None,
        {
            "Authorization": "Bearer %s" %cr_key
        }
        )

        response = urllib.request.urlopen(request).read().decode("utf-8")
        data = json.loads(response)
        #newTrophies = data['items'][0]['trophies']

        try:
            newTrophies = data['items'][0]['trophies']
        except IndexError:
            newTrophies = 0

        print(str(newTrophies) + " - " + str(loc))
        if newTrophies > trophies:
            tag = data['items'][0]['tag']
            name = data['items'][0]['name']
            trophies = newTrophies
            print("Leader is " + name + " (" + tag + ") with " + str(trophies) + " trophies.")
            pass
        loc +=1
        time.sleep(3)
        pass

    pass
