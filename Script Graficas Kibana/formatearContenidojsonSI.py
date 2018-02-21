import tweepy
import sys
import json
from tweepy import OAuthHandler
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch
import re

es = Elasticsearch([{'host' : 'localhost', 'port' : 9200}])

arch = open('datossi.json',"r")
arch1 = open('datossiFormato.json',"wr")
contenido = arch.readlines()
print len(contenido)
for x in contenido:
	x = x.replace('{"_index":"votosi","_type":"_doc","_id":"','')
	x = x.replace('","_score":1,"_source":{','{')	
	x = x.replace('}}', ', "voto": "si"}')
	y = re.sub('([0-9]+{+)','{',x)
	#print y
	arch1.write(y)


