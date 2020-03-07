from tweepy import Stream
from tweepy.streaming import StreamListener
from user import *
import tweepy
from tweepy import Cursor
from tweepy import API
import numpy as np
import pandas as pd


class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_fiend):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_fiend):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = tweepy.OAuthHandler(COMSUMER_KEY, COMSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth


class TwitterSteamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, tweets_fileName, hash_tag_list):
        listener = TwitterListener(tweets_fileName)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)


class TwitterListener(StreamListener):
    def __init__(self, tweets_fileName):
        self.tweets_fileName = tweets_fileName

    def on_data(self, data):
        try:
            print(data)
            with open(self.tweets_fileName, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            return False
        print(status)


class TwitterAnalyse():
    # Funtionality for analyzing and categorizing content from tweets.
    def twitter_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Text'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        return df


if __name__ == '__main__':
    '''
    twitter_client = TwitterClient()
    twitter_analyse = TwitterAnalyse()
    api = twitter_client.get_twitter_client_api()
    tweets = api.user_timeline(screen_name="", count=20)
    df = twitter_analyse.twitter_to_data_frame(tweets)
    df.to_csv('anhyeuem.csv', index=None)
    '''


    hast_tag_list = ["covid 19"]
    tweets_fileName = "tweets.json"
    twitter_streamer = TwitterSteamer()
    twitter_streamer.stream_tweets(tweets_fileName, hast_tag_list)
