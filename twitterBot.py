# libraries
import tweepy
import requests
import os
import time
from datetime import date

# keys and key auth
CONSUMER_KEY = 'ENTER_KEY_HERE'
CONSUMER_SECRET = 'ENTER_KEY_HERE'
ACCESS_KEY = 'ENTER_KEY_HERE'
ACCESS_SECRET = 'ENTER_KEY_HERE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
img_url = "https://i.giphy.com/media/0GiS2YnPUo1xzG4cpP/giphy.webp"
tweet = "Happy Monday!"
twitter_API = tweepy.API(auth)


def post_gif(url, tweet, twitter_API):
    if date.today().weekday() == 0:
        image_tweet(url, tweet, twitter_API)

def image_tweet(url, tweet, twitter_API):
    api = twitter_API
    file = 'image.gif'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(file, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(file, status=tweet)
        os.remove(file)
    else: 
        print("error in image")


while(True):
 post_gif(img_url, tweet, twitter_API)
 time.sleep(86400) # daily tweet




