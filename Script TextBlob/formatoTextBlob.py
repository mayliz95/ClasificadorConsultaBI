import sys
import json
import re

arch = open('votos.json',"r") 
arch2 = open('votosJSON.json',"wr")
res = open('votosFormato.txt',"wr")
contenido= arch.readlines()

arch2.write('[')
i=1
for x in contenido:
	if(i == len(contenido)):
		arch2.write(x)
	else:
		arch2.write(x + ',')
	i=i+1
arch2.write(']')	

arch2.close()

url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
url2= '(www\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
emoticons= "['\&\-\.\/()=:;]+"
patron = re.compile('#|@|'+url+'|'+url2+'|'+emoticons)

leer = json.loads(open('votosJSON.json').read())
i=1
for y in leer:
	texto = y['text']
	voto = y['voto']
	tx = patron.sub(' ',texto)
	#print '(' + tx + ', ' + voto+')'
	if(i == len(contenido)):
		res.write("('" + tx + "', '" + voto+"')\n")
	else:
		res.write("('" + tx + "', '" + voto+"'),\n")
	i=i+1