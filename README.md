#ESCUELA POLITÉCNICA NACIONAL 

#FACULTAD DE INGENIERÍA DE SISTEMAS

#INTELIGENCIA DE NEGOCIOS

Objetivo General:
==========
 Implementar e investigar el funcionamiento de un clasificador de sentimientos utilizando los algoritmos de aprendizaje vistos en clase y los datos recolectados de Twitter para identificar tendencias de opinión en las 3 ciudades más importantes del país por el tema de “CONSULTA POPULAR” del domingo 4 de febrero de 2018. 
 
 Objetivo Especifico:
==========
   Crear un clasificador de sentimiento en español utilizando datos extraídos de Twitter para minar opinión pública en las ciudades de Quito, Guayaquil y Cuenca. 

   Identificar y seleccionar las herramientas necesarias para procesar y analizar datos en tiempo real provenientes de Twitter 
 
Integrantes:
--------------------
- Mayra Rosero
  
- Graciela Moreno

Herramientas:
--------------------

- Python 2.7 - Lenguaje utilizado.

- ElasticSearch - Herramienta de Map - Reduce.

- Kibana - Presentación de Gráficos.

Fases del proyecto 
--------------------
La metodología a ser utilizada necesita que se investigue, seleccione, implemente y desarrolle distintos procedimientos para el análisis de tendencias con datos relacionados a la consulta. El principal énfasis que se hace en el presente trabajo es el análisis en español y por los hagtash. 

- Adquisicion de Datos

- Pre-procesamiento de Datos

- Procesamiento de Datos

- Análisis de Datos

- Presentación de Datos

Adquisición de datos 
--------------------

Para esta fase es necesario recolectar datos utilizando un cosechador de tweets entregado al inicio de este curso a través del aula virtual. En dicho cosechador, se establecieron las coordenadas necesarias para capturar tweets correspondientes a la ciudad de Quito Las herramientas utilizadas para esta fase corresponden a un script codificado en Python y una base de datos noSQL(CouchDb). 

Para esta fase se realizaran los siguientes pasos: 

- Instalación couchdb 

- Creación BD 

- Recolectar tuits: harverster_uio (3 archivos, uno por cada ciudad) 

 

Pre-procesamiento 
--------------------

Será necesario filtrar los tweets correspondientes a las ciudades de Quito, Guayaquil y Cuenca, utilizando vistas en la base de datos o cualquier otra técnica que ustedes consideren conveniente. Además, será necesario filtrar tweets únicamente correspondientes al idioma español. 

Para realizar el pre-procesamiento se ha seguido los siguientes pasos:  

- Creación de una vista que filtra por ciudades (place.name) y por lenguajes (lang) 

- Guardar en archivo todos los tuits solo con campos necesarios texto, ciudad, lenguaje, limpiarlos de emojis (conn_couch) -- Tratar de poner full_text de extended_tweet 

 
Clasificación de tweets 
------------------------

- Id:Código identificador de tweet 

- Texto :Contenido del mensaje del tweet 

- Coordenadas:Contenido de las coordenadas de publicación del tweet 

- Lang :Idioma en el que es publicado el tweet 

- hashtag  :Hashtag nombrado en el texto del mismo. Si hubiese varios, solo guarda el primero que encuentre.  

- place.name:El nombre del lugar de publicación del tweet 
 

Procesamiento 
---------------

Una vez que se tengan los tweets, será necesario procesar su campo “texto” para poder determinar la opinión pública respecto a la consulta popular. El procesamiento de texto de un tweet generalmente involucra la remoción de caracteres especiales, links, tags, etc. En este caso será necesario identificar y  

El procesamiento de los tweets se realiza con los pasos: 

- filtrar los tweets relacionados a la consulta popular. 

- Colocar los tuits en elasticsearch (elastweets.py) 

- Obtener los tuits referentes a la consulta 

- Colocar los tuits en elasticsearch solo de la consulta 

- Filtrar los que tienen tendencia a si y los que tienen tendencia a no 

- Probar en un clasificador como textblob 

Análisis 
---------

Es necesario realizar un análisis sobre el texto de cada tweet, para minar la opinión pública de las 3 ciudades. En este caso se deberá diseñar un clasificador en español que permita identificar la tendencia del voto por el sí o por el no en cada ciudad de tal forma que se logre una exactitud de clasificación alta. En este sentido será muy importante determinar las características necesarias (i.e vector de características) del data set de entrenamiento para lograr una alta exactitud de clasificación 

Para la realización del análisis se generara: 

- Mostrar resultados Graficamente (línea de tiempo, mapa de calor y diagramas de pastel) 

 
Presentación 
-------------

 Para esta fase se utilizara kibana para generar graficas de pasteles para ver los porcentajes del si y del no tanto en Quito ,Guayaquil y CUenca ,mapas de calor que nos permitira identificar las zonas en las que se a realizado mayor post de tuits realcionados con la consukta y una linea de tiempo donde se podrta evidenciar el rango de tiempo durante el cual se recolecto los datos y ademas cual es el dia en el que mas tuits relacionados con la consta se tiene,lo mismo que nos permitira ver de mejor manera los resultados obtenidos ,asi como tambien realizar un analisis mas descriptivo.
