import json
import twitter
from user import *

auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, COMSUMER_KEY, COMSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)


def twitter_search(q, max_results, **kw):
    search_results = twitter_api.search.tweets(q=q, count=200, **kw)
    statuses = search_results['statuses']
    max_results = min(1000, max_results)
    for _ in range(100):
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e:
            break
        kwarg = dict([kv.split('=') for kv in next_results[1:].split('&')])
        search_results = twitter_api.search.tweets(**kwarg)
        statuses += search_results['statuses']
        if len(statuses) > max_results:
            break
    return statuses


q = ['Covid-19']
results = twitter_search(q, 1000)
text = [result['text'] for result in results]
print(len(text))
