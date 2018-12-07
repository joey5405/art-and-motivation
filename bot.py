import time
import tweepy
from tweepy import OAuthHandler
from os import environ


from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = OAuthHandler(ck, csk)
auth.set_access_token(oat,oats)
api = tweepy.API(auth)

api.update_status("")
time.sleep(5)