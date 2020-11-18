#import tweepy
#from tweepy.streaming import StreamListener
import json

# Accessing twitter credentials from twitter_account.json (look into the doku to see how to make your own file)
with open("twitter_account.json") as file:
    creditals = json.loads(file.read().strip("\n"))
print(creditals["email"])