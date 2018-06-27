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
 dataset1=pd.DataFrame(get_tweets('realDonaldTrump'))

import numpy as np
c = np.random.randint(0,2,20)
dataset1['Liked']=c

# Cleaning the texts

import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0,20):
    review = re.sub('[^a-zA-Z]', ' ', dataset1[0][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)


# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset1.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
