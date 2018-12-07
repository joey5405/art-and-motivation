import time
import tweepy
from tweepy import OAuthHandler
from os import environ


#ck = '78XhHsIjIsFUn2qhUI0rwSKcA' #(API key)
#csk = 'cH3WvmIUXGdqVtwrMho0sbPQQGTLlpUB4XJ1LusVJetb7dNmKZ' #(API secret key)
#oat = '1068347698284236800-XkscYACRZXnNuBJQAQMZ40Ck4CykWr' #(Access token)
#oats = 'pXADhvlfoWAc95STBHSEIksMl4QD12EmmdzVN09eB1A6e' #(Access token secret)

ck = ''
csk = ''
oat = ''
oats = ''

auth = OAuthHandler(ck, csk)
auth.set_access_token(oat,oats)
api = tweepy.API(auth)

api.update_status("")
time.sleep(5)