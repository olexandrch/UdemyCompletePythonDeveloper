#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 232. Our First Twitter Bot

# https://www.tweepy.org/
# https://developer.twitter.com/en/portal/dashboard

# pip install tweepy
import tweepy
import time

TWITTER_KEYS = '/home/alex/.ssh/twitter-api.keys'

def api_secret(key):
    """ Return Twitter API secrets. Allowed requests are:
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

def limit_handler(cursor):
    """Limit API access speed. If we hit the rate limit pause for 3s"""
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(3)
    except StopIteration:
        StopIteration


# Print names of the followers 
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(f'You are followed by {follower.name}, who has {follower.followers_count} followers')

print('='*20)

# Print names of your friends (people you follow)
for friend in limit_handler(tweepy.Cursor(api.friends).items()):
    print(f'You are following {friend.name}, who has {friend.followers_count} followers')

# Search and like tweet defined by 'search_string'
search_string = 'python'
number_of_twits = 2

for twit in limit_handler(tweepy.Cursor(api.search, search_string, lang='en').items(number_of_twits)):
    try:
        # uncomment 'twit.favorite()' if you want to actually like the tweets
        # twit.favorite()
        print(f'I liked tweet')
    except tweepy.TweepError as e:
        print(f'I got en error: {e}')

print('='*20)

# Tweet 
api.update_status("This is a message by my twitter bot! Thanks to tweepy python library!")
print("I just twitted. You should see the twit as first message on the timeline below!!!")


print('='*20)

# Print twits from my timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

print('='*20)

# Print info about me
user = api.me()

print ('user.name: ', user.name)
print ('user.screen_name: ', user.screen_name)
print ('user.followers_count: ', user.followers_count)
print ('user.location: ', user.location)
