#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:56:46 2020

@author: shachi
"""

import tweepy
from tweepy import OAuthHandler
import re

import config

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
 

api = tweepy.API(auth)

def clean_text(text):
    text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
    text = re.sub('#', '', text) # Removing '#' hash tag
    text = re.sub('RT[\s]+', '', text) # Removing RT
    text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
 
    return text

def de_emojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

search_results = tweepy.Cursor(api.search, q = "netflix", lang='en').items(5)

for result in search_results:
    r = clean_text(result.text)
    r = de_emojify(r)
    user = result.author.screen_name
    tweetId = result.id
    tweetUrl = "https://twitter.com/" + str(user) + "/status/" + str(tweetId)
    print(r)
    print(tweetUrl)
    
