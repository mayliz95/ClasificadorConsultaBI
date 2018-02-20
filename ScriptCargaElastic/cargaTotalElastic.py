import tweepy
import sys
import json
from tweepy import OAuthHandler
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch


es = Elasticsearch([{'host' : 'localhost', 'port' : 9200}])

arch = open('tuitslimpios.json',"r")
contenido = arch.readlines()
i=0
print len(contenido)
for x in contenido:
	#print x
	es.index(index="consulta_popular", doc_type="_doc", id=i, body=x, ignore=400)
	i = i+1

