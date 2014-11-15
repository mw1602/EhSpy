import tweepy
import os
from firebase import *
import json


auth = tweepy.OAuthHandler(os.environ['consumer_token'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'], os.environ['access_secret'])
f = firebase.FirebaseApplication('https://expat-finder.firebaseio.com/', None)


class StdOutListener(tweepy.streaming.StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        if decoded['geo'] and decoded['lang'] == 'en' and decoded['place']['country'] == 'United States':

            
            x, y = decoded['geo']['coordinates']
            tweet = decoded['text']
            # print coords
            # print decoded['place']['country']
           

            
            self.store_data((x,y,tweet))
            # print json.dumps(decoded, indent = 4, separators=(',', ': '))


    def store_data(self, coords):
        f.post('/coordinates', coords)



    def on_error(self, error):
        print error

if __name__ == '__main__':
    l = StdOutListener()
    stream = tweepy.Stream(auth,l)
    stream.filter(track=['eh'], )




