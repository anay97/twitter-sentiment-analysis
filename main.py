import tweepy
from textblob import TextBlob

#You can get these from dev.twitter.com
consumer_key='my-cons-key'
consumer_secret='my-cons-secret'


access_token='my-access-token'
access_token_secret='my-access-token-secret'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

#Collect tweets
sum=0
count=0
public_tweets=api.search('Gandhi')
for tweet in public_tweets:
  #print tweet.text
  analysis=TextBlob(tweet.text)
  #print(analysis.sentiment)
  sum=sum+analysis.sentiment.polarity
  count=count+1
print("Polarity:"+str(sum/count))