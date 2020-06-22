import twitter
def find_popular_tweets(twitter_api, statuses, retweet_threshold=3):
 # You could also consider using the favorite_count parameter as part of
 # this heuristic, possibly using it to provide an additional boost to
 # popular tweets in a ranked formulation

 return [ status
 for status in statuses
 if status['retweet_count'] > retweet_threshold ]

# Sample usage
q = "CrossFit"
twitter_api = oauth_login()
search_results = twitter_search(twitter_api, q, max_results=200)
popular_tweets = find_popular_tweets(twitter_api, search_results)
for tweet in popular_tweets:
 print tweet['text'], tweet['retweet_count']