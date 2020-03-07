import tweepy
from user import *


def api():
    # creating the authentication object
    auth = tweepy.OAuthHandler(COMSUMER_KEY, COMSUMER_SECRET)
    # setting your access token and secret
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api
