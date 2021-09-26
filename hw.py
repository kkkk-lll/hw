#!/usr/bin/env python
# encoding: utf-8
import json
import requests
import os
import tweepy

#Bearer Token
#AAAAAAAAAAAAAAAAAAAAAPNdUAEAAAAAW0Cyw2FNbHJQSN3Tsdpayx2f2VE%3DP6B400SGslbLMaPcK3vozkS0tX353TdWFYoXM7MCUGXA8vkRHm

#declare the keys and secrets
consumer_key = "XD5LPTbAmtJLyTDssVnxnOs82" #"the consumer key"
consumer_secret = "mWYdVvNeyIwdQ22Mh5vEbuihwkWjhpNZPsx2tfuoD6dQMgdK5O"# "the consumer secret"
access_key = "the consumer key" #acess的key我还没找到，正在找！
access_secret = "the access_secret"

#authorize
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

#iinitialize
api = tweepy.API(auth)

keywords = "your keyword"
start_time = "start time"
number = "the number of tweets"

for tweet in tweepy.Cursor(api.search, q=keywords, lang="en", since=start_time).items(number):
	    tweets=[tweet.user.screen_name]
 
