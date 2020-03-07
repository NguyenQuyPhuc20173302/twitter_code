import tweepy
import json
import pandas as pd
import API_twitter
from collections import Counter

api = API_twitter.api()
new_search = ['Covid 19']
tweets = tweepy.Cursor(api.search, q=new_search, lang='en').items(2000)
text = [tweet.text for tweet in tweets]
for t in text:
    print(t)
'''
statuses = [tweet.entities for tweet in tweets]

hashtags = []
for status in statuses:
    for hashtag in status['hashtags']:
        hashtags.append(hashtag['text'])
c = Counter()
for i in hashtags:
    c[i] += 1

'''
words = []
for t in text:
    for w in t.split():
        words.append(w)
c = Counter()
for item in words:
    c[item] += 1
'''
from prettytable import PrettyTable

pt = PrettyTable()
pt.field_names = ['Word', 'Count']
for word in c.most_common(10):
    pt.add_row(word)
print(pt)
'''