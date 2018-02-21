import tweepy
import sys
import json
from tweepy import OAuthHandler
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch
import re

es = Elasticsearch([{'host' : 'localhost', 'port' : 9200}])

arch = open('datosno.json',"r")
arch1 = open('datosnoFormato.json',"wr")
contenido = arch.readlines()
print len(contenido)
for x in contenido:
	x = x.replace('{"_index":"votono","_type":"_doc","_id":"','')
	x = x.replace('","_score":1,"_source":{','{')	
	x = x.replace('}}', ', "voto": "no"}')
	y = re.sub('([0-9]+{+)','{',x)
	#print y
	arch1.write(y)


