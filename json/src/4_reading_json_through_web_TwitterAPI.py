import tweepy
import json

def auth(access_token, access_token_secret, consumer_key, consumer_secret):
    """ Passing credentials to tweepy's OAuth handler """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    return auth

def stream(auth):
    l = MyStreamListener()
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['keyword1', 'keyword2', 'keyword3', 'keyword4'])
    return stream

def main():
    # credentials
    access_token = "pass"
    access_token_secret = "pass"
    consumer_key = "pass"
    consumer_secret = "pass"

    # API authentication
    auth = auth(access_token, access_token_secret, consumer_key, consumer_secret)
    # fetch some data
    data = stream(auth)

if(__name__ = '__main__'):
    main()
