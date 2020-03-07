from tweepy import Stream
from tweepy.streaming import StreamListener
from user import *
import tweepy
from tweepy import Cursor
from tweepy import API
import numpy as np
import pandas as pd

list_id = []
list_len = []
list_date = []
list_likes = []
list_source = []
list_text = []


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = tweepy.OAuthHandler(COMSUMER_KEY, COMSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth


class TwitterSteamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, hash_tag_list):
        listener = TwitterListener()
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list, languages=["en"])


import json


class TwitterListener(StreamListener):
    def __init__(self):
        pass

    def on_data(self, data):
        df = pd.DataFrame()
        data = json.loads(data)
        list_id.append(data['id'])
        list_len.append(len(data['text']))
        list_date.append(data['created_at'])
        list_source.append(data['source'])
        list_likes.append(data['favorite_count'])
        list_text.append(data['text'])
        df['id'] = list_id
        df['len'] = list_len
        df['date'] = list_date
        df['likes'] = list_likes
        df['source'] = list_source
        df['text'] = list_text
        if len(list_id) == 10:
            df.to_csv('data_covid19.csv', index=None)
            exit()
        return True

    def on_error(self, status):
        if status == 420:
            return False
        print(status)


if __name__ == '__main__':
    hast_tag_list = ["Covid 19"]
    twitter_streamer = TwitterSteamer()
    twitter_streamer.stream_tweets(hast_tag_list)
