ESCUELA POLITÉCNICA NACIONAL 
==========
FACULTAD DE INGENIERÍA DE SISTEMAS
==========
INTELIGENCIA DE NEGOCIOS
==========
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

- ElasticSearch 6.2.1 - Herramienta de Map - Reduce.

- Kibana 6.2.1 - Presentación de Gráficos.

- ElasticDump - Backup Índices elasticsearch

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

- Script para recolectar tuits: [Recolectores Tuits](https://github.com/mayliz95/ClasificadorConsultaBI/tree/master/Scripts%20Recolectar%20Tuits)  (3 archivos, uno por cada ciudad) 
 

Pre-procesamiento 
--------------------

Será necesario filtrar los tweets correspondientes a las ciudades de Quito, Guayaquil y Cuenca, utilizando vistas en la base de datos o cualquier otra técnica que ustedes consideren conveniente. Además, será necesario filtrar tweets únicamente correspondientes al idioma español. 

Para realizar el pre-procesamiento se ha seguido los siguientes pasos:  

- Creación de una [vista](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/vista.txt) que filtra por ciudades (place.name) y por lenguajes (lang) 

- Guardar en archivo todos los tuits solo con campos necesarios texto, ciudad, lenguaje, coordenadas, país, fecha de creación y texto completo. Además, se limpió de emojis el texto con este [Script](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/conn_couch_up.py)

 
Clasificación de tweets 
------------------------

- Id:Código identificador de tweet 

- Texto :Contenido del mensaje del tweet 

- Coordenadas:Contenido de las coordenadas de publicación del tweet 

- Lang :Idioma en el que es publicado el tweet 

- Created_at: Fecha de creación del tweet.

- place.name:El nombre del lugar de publicación del tweet 
 

Procesamiento 
---------------

Una vez que se tengan los tweets, será necesario procesar su campo “texto” para poder determinar la opinión pública respecto a la consulta popular. Será necesario identificar y filtrar los tweets relacionados a la
consulta popular.

El procesamiento de los tweets se realiza con los pasos: 

- Creación de un índice en elasticsearch, se ejecuta el [Script](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/ScriptCargaElastic/MappingTweet) en el terminal con curl o en la consola de Kibana.

- Colocar los tuits en elasticsearch con el [Script](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/ScriptCargaElastic/cargaTotalElastic.py)

- Crear un índice en elasticsearch para los tweets referentes a la consulta con el [Script](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20Tuits%20Consulta/creaIndiceConsulta.txt), este se ejecuta en el terminal con curl o en la consola de Kibana.

- Filtrar los tuits referentes a la consulta y reindexarlos al índice creado en el paso anterior con el [Script](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20Tuits%20Consulta/reindexacionTuisConsulta.txt) 

Análisis 
---------

Es necesario realizar un análisis sobre el texto de cada tweet, para minar la opinión pública de las 3 ciudades. En este caso se deberá diseñar un clasificador en español que permita identificar la tendencia del voto por el sí o por el no. 

- Obtener tuits que tienen tendencia a si con los [Scripts] (https://github.com/mayliz95/ClasificadorConsultaBI/tree/master/Scripts%20Tuits%20Votos/VotaSi)

- Obtener tuits que tienen tendencia a no con los [Scripts](https://github.com/mayliz95/ClasificadorConsultaBI/tree/master/Scripts%20Tuits%20Votos/VotaNo)

- Obtener Json con contenido de índices no y si, se ejecuta en el terminal los [comandos] (https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20Graficas%20Kibana/comandosElasticDump.txt) de elasticdump

- Formatear el contenido de los archivos json, para el [no](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20Graficas%20Kibana/formatearContenidojsonNO.py) y para el [si](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20Graficas%20Kibana/formatearContenidojsonSI.py)

- Se une ambos archivos generados utilizando el [Script](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20Graficas%20Kibana/cargarDatosKibana.py)

- Se da el formato necesario a los tweets para colocarlos en textblob, es decir se toma el texto y la tendendencia de voto con el [Script](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20TextBlob/formatoTextBlob.py)

- Se realiza un análisis del dataset al que se llego con el [clasificador_precisión](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20TextBlob/Clasificador_accurrancy.py)

Presentación 
-------------

Para esta fase se utilizara Kibana para generar graficas de pasteles para ver los porcentajes del si y del no tanto en Quito ,Guayaquil y Cuenca ,mapas de calor que nos permitira identificar las zonas en las que se a realizado mayor post de tuits relacionados con la consulta y una linea de tiempo donde se podrta evidenciar el rango de tiempo durante el cual se recolecto los datos y ademas cual es el dia en el que mas tuits relacionados con la consulta y con tendencia de voto se tiene,lo mismo que nos permitira ver de mejor manera los resultados obtenidos ,asi como tambien realizar un analisis mas descriptivo.

Para ello, se realiza lo siguiente:

- Creación de un índice con el [comando](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20Graficas%20Kibana/mappingVotos.txt) ejecutando en el terminal con curl o en la consola de Kibana

- Cargar los tweets al índice creado en el paso anterior con el [Script](https://github.com/mayliz95/ClasificadorConsultaBI/blob/master/Script%20Graficas%20Kibana/cargarDatosKibana.py)

- Realizar en Kibana los gráficos requeridos mediante la interfaz gráfica.
