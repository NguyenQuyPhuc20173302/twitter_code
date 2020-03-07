from API_twitter import *

#   using API object to get tweets from your homeLine, and storing it in a variable calls public_tweets
api = api()
public_tweets = api.home_timeline(count=100)
for tweet in public_tweets:
    # Process a single status
    print(tweet.text)

print()
# get friend list on the twitter
for friend in tweepy.Cursor(api.friends).items():
    print(friend._json)

