# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "FQ77UMLjKRgcoFSyTASzwixnI"
consumer_secret = "1qVi8JYhEUU3xAWVnrL99AUznEWOIuQWKZH8J1KkxWjtC24qL0"
access_token = "969400125805047808-yAN8pR7wneqdTr3CW4of1651vJmU5IV"
access_token_secret = "vuxPy8mfIk3XcIUPoczSFUAfgvEtaQNpZ1q843miRPNJ3"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERES