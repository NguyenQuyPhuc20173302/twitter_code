import tweepy
import pandas as pd
import API_twitter

list_id = []
list_date = []
list_text = []
list_language = []


def append_data(tweets):
    for tweet in tweets:
        list_text.append(tweet.text)
        list_id.append(tweet.id)
        list_date.append(tweet.created_at)
        list_language.append(tweet.lang)


def get_list_data(tweets):
    try:
        append_data(tweets)
        df = pd.DataFrame()
        df['ID'] = list_id
        df['Date'] = list_date
        df['Language'] = list_language
        df['Text'] = list_text
        df.to_csv('data_Covid19.csv', index=None)
    except BaseException as e:
        get_list_data(tweets)


api = API_twitter.api()
new_search = ['Covid 19']
tweets = tweepy.Cursor(api.search, q=new_search, lang='en').items(1000)
get_list_data(tweets)
