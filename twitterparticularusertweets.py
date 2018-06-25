# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:33:23 2018

@author: Karan Sharma
"""
#Getting tweets from particular person.
# Importing the dataset
import tweepy
from tweepy import OAuthHandler

consumer_key = 'HbMx25T*****r8TrZ'
consumer_secret = 'NWKoZiS12********5FwWX7lMd6qJohEJGFS'
access_token = '3545155273-hd********2GqubpUmsJFh4'
access_secret = 'qp9Ay84MTAs******AACoM2c7'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#example 2

# Function to extract tweets
def get_tweets(username):
         
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
        # Access to user's access key and access secret
        auth.set_access_token(access_token, access_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
    
        tweets = api.user_timeline(screen_name=username)
 
        # Empty Array
        tmp=[] 
 
        # create array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
        for j in tweets_for_csv:
 
            # Appending tweets to the empty array tmp
            tmp.append(j) 
 
        # Printing the tweets
        print(tmp)
        return tmp
 
a=get_tweets('narendramodi')