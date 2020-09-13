#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 232. Our First Twitter Bot

# https://www.tweepy.org/
# https://developer.twitter.com/en/portal/dashboard

# pip install tweepy
import tweepy

TWITTER_KEYS = '/home/alex/.ssh/twitter-api.keys'

def api_secret(key):
    """ Return Twitter API secrets on return to 
    'API key', 'API secret key', 'Access token', 'Access token secret'"""
    with open(TWITTER_KEYS, 'r') as reader:
        while (line := reader.readline().strip()) != '':
            api_key, secret = line.split(':')
            if key == api_key:
                return secret
        return None

auth = tweepy.OAuthHandler(api_secret('API key'), api_secret('API secret key'))
auth.set_access_token(api_secret('Access token'), api_secret('Access token secret'))

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.me()

print (user.name)
print (user.screen_name)
print (user.followers_count)
