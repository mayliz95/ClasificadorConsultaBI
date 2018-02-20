'''

 
GUAYAQUIL
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
 
##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter
ckey = "n463euMexgTZ2ZnKwYxgXGwfj"
csecret = "aLYHZdAOwiVfq0014yVe14zSQxXb8Zqn0wVaLbTvtoFYW6LSZI"
atoken = "945462108346560512-3HPqfiMBwpcbb5h3zjH9aMLtHf0h3nO"
asecret = "NcPxYtqVHPhljprG3KqdCulcJaaHcnfmUo5UFon2S1YKa"

class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
 
    def on_error(self, status):
        print status
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
 
 
#if len(sys.argv)!=3:
 #  sys.stderr.write("Error: needs more arguments: <URL><DB name>\n")
#  sys.exit()
 
#URL = sys.argv[1]
#db_name = sys.argv[2]

URL = '127.0.0.1'
db_name = 'db_guayaquil'
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''
track_terms = ['#dilesialfuturo', '#votatodosi', '#7vecessi', '#dilesno', '#ConsultaPopular', '#PorLaPatriaDilesNO', '#7vecesno', 'vota no', 'vota si']
twitterStream.filter(locations=[-79.93824,-2.195355,-79.892921,2.161047],track=track_terms)  #GUAYAQUIL

#track_terms = ['#dilesialfuturo', '#votatodosi', '#7vecessi', '#dilesno', '#ConsultaPopular', '#PorLaPatriaDilesNO', '#7vecesno']
#twitterStream.filter()
