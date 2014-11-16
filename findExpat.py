import tweepy
import os
from firebase import *
import json
import re


auth = tweepy.OAuthHandler(os.environ['consumer_token'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'], os.environ['access_secret'])
f = firebase.FirebaseApplication('https://expat-finder.firebaseio.com/', None)


class StdOutListener(tweepy.streaming.StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        if decoded['geo'] and decoded['lang'] and decoded['place']: #and decoded['place']['country'] == 'United States':

            
            x, y = decoded['geo']['coordinates']
            tweet = decoded['text']  
            # print tweet     

            if decoded['lang'] == 'en' and decoded['place']['country'] == 'United States': 

                # print json.dumps(decoded, indent = 4, separators=(',', ': '))
                
                print tweet

                if self.isCanadian(tweet):
                    self.store_data((x,y,tweet))


    def store_data(self, coords):
        f.post('/coordinates', coords)



    def on_error(self, error):
        print error

    def isCanadian(self, tweet):

        # c= re.compile("t")
        c = re.compile("(\\beh\?|,eh\?)", re.I)
        canadian = c.search(tweet)
        if canadian:
            return True
        else: return False
        #might do something something fancier here later to handle complicated 'eh' situations



if __name__ == '__main__':
    l = StdOutListener()
    stream = tweepy.Stream(auth,l)
    stream.filter(track=['eh'], )




