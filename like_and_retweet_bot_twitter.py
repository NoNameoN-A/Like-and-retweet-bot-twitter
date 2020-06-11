import tweepy
import time

auth = tweepy.OAuthHandler('API_key:','API_secret_key')

auth.set_access_token('Access_token','Access_token_secret')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'hashtag'
nrTweets = 500


for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        tweet.retweet()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
