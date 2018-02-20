# -*- coding: utf-8 -*-
import couchdb
import sys
import urllib2
import json
import re


URL = 'localhost'
db_name = 'consulta' 	#Nombre de la base en couchdb


'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

#url = 'http://localhost:5984/bi_database/_design/vistaprueba/_view/vistaprueba'
url = 'http://localhost:5984/consulta/_design/quito_cuenca_guayaquil/_view/new-viewQGC_ES' 	#Ruta de la vista en couchdb

req = urllib2.Request(url)
f = urllib2.urlopen(req)
print (f)
d = json.loads(f.read())

arch = open('tuitslimpios.json',"wr") #Tuits sin emojis ni caracteres RAROS!!
arch.write('[\n')
numfil = d['total_rows'] 
i=1
for x in d['rows']:
    
    text = x['value']['text']
    ciudad = x['value']['place']['name']
    leng = x['value']['lang']
    if (x['value']['coordinates'] != None):
    	location = x['value']['coordinates']['coordinates']
    else:
    	location = '""'
    if (x['value'].has_key('extended_tweet')):    	
    	full_text = x['value']['extended_tweet']['full_text']
    else:
    	full_text = ""
    country = x['value']['place']['country']
    created_atM = x['value']['created_at']
    created_at = created_atM.replace("+0000 ", "")

    #tex_limp = re.sub('[^0-9a-zA-Z:/#@.,?!ñáéíóúÑÁÉÍÓÚ 	]','',text)
    tex_limp = re.sub('[^0-9a-zA-Z:/#@.,?! ]','',text)
    ftext_limp = re.sub('[^0-9a-zA-Z:/#@.,?! ]','',full_text)    
    arch.write('\t{"location": '+ str(location) + ', "extended_tweet": {"full_text": "'+ ftext_limp +'"}, "lang": "' + leng + '", "place": { "country": "' + country +'", "name": "' + ciudad +'"}, "text": "' + tex_limp +'", "created_at" : "' + created_at +'"}\n')
    #print '\t{"location": '+ str(location) + '", "extended_tweet": {"full_text": "'+ ftext_limp +'"}, "lang": "' + leng + '", "place": { "country": "' + country +'", "name": "' + ciudad +'"}, "text": "' + tex_limp +'", "created_at" : "' + created_at +'"}\n'
    #print (i)
    i = i+1
arch.write(']')
