import tweepy
import sys
import json
from tweepy import OAuthHandler
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch


es = Elasticsearch([{'host' : 'localhost', 'port' : 9200}])

arch = open('votos.json',"wr")
a1 = open('datosnoFormato.json',"r")
c1= a1.readlines()
i=1
for no in c1:
	arch.write(no)
	print i
	i=i+1
a2 = open('datossiFormato.json',"r")
c2 = a2.readlines()
j=1
for si in c2:
	arch.write(si)
	print j
	j=j+1
arch.close()
arch = open('votos.json',"r")
contenido = arch.readlines()
i=0
print len(contenido)
for x in contenido:
	#print x
	es.index(index="votos", doc_type="_doc", id=i, body=x, ignore=400)
	i = i+1

