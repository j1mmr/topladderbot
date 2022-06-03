import os
import time

from dotenv import load_dotenv, find_dotenv

#requires pip package python-find_dotenv

import tweepy

import urllib.request
import json

load_dotenv(find_dotenv())

#Clash Royale api setup
cr_key = os.getenv('crKey')
base_url = "https://api.clashroyale.com/v1/locations/"
endpoint = "/rankings/players?limit=1"


#tweepy and twitter api setup
CONSUMER_KEY = os.getenv('consumerKey')
CONSUMER_SECRET = os.getenv('consumerSecret')
ACCESS_KEY = os.getenv('accessKey')
ACCESS_SECRET = os.getenv('accessSecret')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

currentTag = ''

while (True):
    statement = ''
    loc = 57000007
    print("starting...")
    trophies = 0
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

        #print(str(newTrophies) + " - " + str(loc))
        if newTrophies > trophies:
            tag = data['items'][0]['tag']
            tagClean = tag[1:]
            name = data['items'][0]['name']
            trophies = newTrophies
            statement = "Leader is " + name + " with " + str(trophies) + " trophies. https://royaleapi.com/player/" + tagClean
            pass
        loc +=1
        time.sleep(2)
        pass

    if tag!=currentTag:
        print("Tweeted: " + statement)
        currentTag = tag
        api.update_status(status = statement)
        pass
    else:
        print("No change")
        pass

    print("done")
    pass
