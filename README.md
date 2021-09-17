# Proyecto Final de Análisis de Datos 

### Integrantes:
###### Benavides Kevin 
###### Guachamín Daniel
###### León Jeremy 
###### Yazán Cindy 
###### Valdivieso Gabriel


Apartir de la siguiente arquitectura data lake, se ha logrado llegar a un respectivo análsis
![ArquitecturaDataLake drawio (1)](https://user-images.githubusercontent.com/66692550/133800860-f7993b5c-9286-484b-8a39-6ce27a093a70.png)

Adicional, el video donde se presenta el proceso de extracción de datos se lo puede encontrar en la siguiente dirección: https://youtu.be/27U1Bu1_oOA
### Empezaremos con el Facebook_ Scraping con el tema Pulso político por provincias

Instalamos la dependencia que necesitaremos para hacer la captura de datos.

![image](https://user-images.githubusercontent.com/66692550/133801722-694b2aa7-fb33-4656-a787-7590bb491593.png)

Importamos las librerías que nos servirán con para la manipulación de los datos

![image](https://user-images.githubusercontent.com/66692550/133801795-fce11745-6147-4bd7-936a-87e2725b4285.png)

Establecemos conexión con la base de datos “COUCHDB” y designamos el nombre de la base de datos que usaremos para la captura.

![image](https://user-images.githubusercontent.com/66692550/133801824-65943545-6b00-4a19-bc5d-d3e4769fdb47.png)

Como siguiente paso primero se tuvo que indagar en la red social “Facebook”, para buscar las páginas que tengan los datos que nosotros necesitaremos para nuestro análisis, entre ellas las páginas directamente propietarias de los partidos políticos con actividades de sus candidatos.

![image](https://user-images.githubusercontent.com/66692550/133802264-1b0f330a-3b44-4619-8e7f-00439b794194.png)

Con los nombres de las páginas que necesitamos y con el script de código en Python ya podemos cosechar los datos a nuestra base de datos, simplemente cambiado el nombre de la página para cada cosecha.

![image](https://user-images.githubusercontent.com/66692550/133802394-689beb37-9266-4bcf-a97e-7678cd10f5cf.png)

Esto hará que tengamos la base de datos con los datos cosechados

![image](https://user-images.githubusercontent.com/66692550/133802464-d0d4c684-82ff-4d9e-93a1-bac21c92e156.png)
![image](https://user-images.githubusercontent.com/66692550/133802474-4cb030ff-c92c-42ba-82f9-faf97fbb16e8.png)

Tenemos listo el archivo JSON, por lo que nos queda descargarlo y pasarlo a nuestra base de datos a utilizar, para descargar de CouchDB utilizamos el siguiente comando.

![image](https://user-images.githubusercontent.com/66692550/133802558-7e8a8953-f3f8-4f73-b874-7168f3656f95.png)

Teniendo el JSON, una página provechosa nos ayudara a crear el script para pasarlo a la base de datos a utilizar que en este caso es SQL SERVER, con unas modificaciones manuales para evitar conflictos y se pueda ejecutar el script sin problema.

![image](https://user-images.githubusercontent.com/66692550/133802608-833e73f6-d42d-4207-aa12-b4511e2ed0b0.png)

Para no tener inconveniente fue necesario cambiar las palabras reservadas que nos arrojó la página como resultado de nuestra transformación, para luego descargar el script.

![image](https://user-images.githubusercontent.com/66692550/133802682-1c30fab7-fb13-40a0-b4a0-c6e0639282b5.png)

Ejecutamos el script para crear la tabla en nuestra BD, SQL SERVER y administrarlo. 

![image](https://user-images.githubusercontent.com/66692550/133802733-8d8ff188-518a-46ef-8502-351507599fab.png)

Y como resultado tenemos nuestra tabla en SQL SERVER con la cosecha de datos.

![image](https://user-images.githubusercontent.com/66692550/133802797-8476cd11-c487-4421-a101-7b0d58416620.png)

El archivo de configuración de jdbc, lograra pasar la tabla de SQL SERVER a elasticsearch y con CEREBRO lo podemos verificar.

![image](https://user-images.githubusercontent.com/66692550/133802825-a57d2015-c806-4580-bf34-267bef0794b8.png)

### Continuamos con Webscraping con el tema seleccionado por los estudiantes (Migración)

El uso de la plataforma INEC se realizó con base en datos migratorios de la siguiente página:

![image](https://user-images.githubusercontent.com/66692550/133803784-d685357f-a314-46c8-b947-dcd544fb3fb3.png)

Para usar esta información se descargó como archivo Excel:

![image](https://user-images.githubusercontent.com/66692550/133803878-d80b7a47-c5a7-4dfe-8bf0-980809a7767b.png)

Del cual se va a extraer las tablas que relación datos como año, género, número de entradas, número de salidas y país de procedencia:

•	Tabla de entradas de ecuatorianos por país de procedencia:

![image](https://user-images.githubusercontent.com/66692550/133804015-30677be9-e9b2-488a-8fd4-3ffdf2e84a4f.png)

•	Tabla de salidas de ecuatorianos por país de destino:

![image](https://user-images.githubusercontent.com/66692550/133804040-ee02d576-6173-45c2-8ad6-6f9e74440121.png)

•	Tabla de entradas de extranjeros por país de procedencia:

![image](https://user-images.githubusercontent.com/66692550/133804064-bfea27be-1ea8-41d8-8655-2e921a1b3e67.png)

•	Tabla de salidas de extranjeros por país de destino:

![image](https://user-images.githubusercontent.com/66692550/133804083-5f6b4c58-d5cd-41dd-b046-4505273936ef.png)

•	Tabla de entradas y salidas generales:

![image](https://user-images.githubusercontent.com/66692550/133804099-382015ea-3fe5-4966-99ce-b1d0c27b9be1.png)

Luego cada una de las tablas fueron transformadas a CSV con Convertio:

![image](https://user-images.githubusercontent.com/66692550/133804197-265004a0-8bd5-4738-abd6-fe5fb08f8604.png)

La siguiente colección creada dentro de una base de datos en MongoDB servirá para importar los archivos CSV extraídos del INEC:

![image](https://user-images.githubusercontent.com/66692550/133804228-4f62a8e6-6a61-4f5f-97d6-48fff26d7de3.png)

Ahora se procede a cargar los archivos:

![image](https://user-images.githubusercontent.com/66692550/133804249-d6b72bde-293c-4675-b00f-6d53d82fc550.png)

Archivos CSV cargados correctamente en MongoDB:

![image](https://user-images.githubusercontent.com/66692550/133804282-747bba5a-d788-4f37-a680-611cd3bfdb79.png)

Para llevar a cabo el WebScraping se ha tomado en cuenta las siguientes páginas, donde se aplicó un script diferentes para cada una, esto se debe a que cambia la forma de filtrar la información:

1.	Ecuador Emigrantes Totales:

El script “Script_WebScraping_1.py” hizo posible el WebScraping de este sitio web (https://datosmacro.expansion.com/demografia/migracion/emigracion/ecuador), donde se obtuvo el DataFrame:

![image](https://user-images.githubusercontent.com/66692550/133804379-cb7417f3-5e8d-4f1a-a8af-c9a20c6b5b88.png)

El cual fue pasado a la base de datos SQLite:

![image](https://user-images.githubusercontent.com/66692550/133804400-9cbc259d-c195-4d4a-b53b-6e35fd688b95.png)

2.	Entradas y salidas internacionales:
El script “Script_WebScraping_2.py” hizo posible el WebScraping de este sitio web (https://www.ecuadorencifras.gob.ec/entradas-y-salidas-internacionales/), donde se obtuvo el DataFrame:

![image](https://user-images.githubusercontent.com/66692550/133804443-fb6d293f-3339-4a23-a8e9-2ef02d5e6c40.png)

El cual fue pasado a la base de datos SQLite:

![image](https://user-images.githubusercontent.com/66692550/133804490-4a230f33-b26c-49be-89ab-99e5518fd809.png)

3.	Luego, se exportó ambas tablas en archivos JSON:

![image](https://user-images.githubusercontent.com/66692550/133804512-a919a84a-0c03-4acd-8df2-dc839308e467.png)

4.	La siguiente colección creada dentro de una base de datos en MongoDB servirá para importar los archivos JSON generados en SQLite:

![image](https://user-images.githubusercontent.com/66692550/133804536-bfd4ce2e-65a1-4190-967b-aba8d0499f98.png)

5.	Luego, se exporta los archivos JSON dentro de la colección establecida:

![image](https://user-images.githubusercontent.com/66692550/133804570-e4d54274-f800-41a1-aca1-c454071a0686.png)

6.	Datos cargados correctamente:

![image](https://user-images.githubusercontent.com/66692550/133804593-aa102566-95c5-4fdb-8c7e-de392fb41494.png)

Cabe destacar que previamente se habían subido los datos extraídos del INEC.
La creación del cluster en ElasticSearch-Cloud se realizó mediante una cuenta colectiva: 

![image](https://user-images.githubusercontent.com/66692550/133804618-f4102d2e-4a7e-4193-bf40-93d739317f84.png)

Esto servirá para unificar los datos de todas las bases de datos creadas.
Para pasar los datos de MongoDB a ElasticSearch-Cloud se usó el archivo .conf “mongodb.conf”:

![image](https://user-images.githubusercontent.com/66692550/133804680-07374917-df2f-4ab6-be51-a6b81f8ab06e.png)

Visualización en Cerebro:

![image](https://user-images.githubusercontent.com/66692550/133804717-090e42f9-7086-486c-b6af-5e1b6f313bef.png)

Una vez exportado como un archivo JSON de SQL Server, el archivo será cargado en una base de datos de CouchDB junto a otro archivo JSON. Esto servirá para unificar la información en una misma base:

![image](https://user-images.githubusercontent.com/66692550/133804765-219080b3-b2a0-4392-9807-4ba9c28ce009.png)

### Twitter Scraping de pulso político por ciudades
Para lograr obtener los datos de twitter se utilizó el script “Cosechando .py”, pero en este caso se utilizaron las palabras claves ('jorge yunda','cynthia viteri', 'quito','guayaquil','cuenca','alcalde quito','alcalde guayaquil','alcalde cuenca') 
De la cual se obtienen una serie de datos

![image](https://user-images.githubusercontent.com/66692550/133804911-111d507b-6cd7-4b21-9ebe-3b4844663e50.png)

Una vez obtenido los datos se procede a enviar los datos a mongodb:

![image](https://user-images.githubusercontent.com/66692550/133819426-d34dcccf-3a50-49a9-b27a-8194e08dc683.png)

![image](https://user-images.githubusercontent.com/66692550/133819533-c607dfec-d2d4-47e5-8e54-cfda62e4cb7c.png)


### Procedemos a obtener datos de Kaggle

Respecto al tema de los juegos en línea por países se ha logrado obtener un dataset de la fuente Kaggle. Los datos encontrados proporcionan información acerca de las ventas de video juegos en diferentes regiones del mundo como se ve en la primera imagen. Sigue la limpieza de la fuente de Kaggle con la herramienta RapidMiner de la segunda imagen. 

![image](https://user-images.githubusercontent.com/66692550/133805285-32f56fa7-37a2-49d1-8490-d72ce3800139.png)

![image](https://user-images.githubusercontent.com/66692550/133805300-edab27b0-b45a-4a8c-9d62-51fe0b09b92b.png)

Los datos obtenidos se los almacena en una base de datos en MongoDB con el nombre de “VideoGamesSales”, los datos están dentro de una colección “videojuegos” como se ve a continuación.

![image](https://user-images.githubusercontent.com/66692550/133805329-078adaa0-9ade-4b58-ac08-f2eb30ee32bc.png)

El proceso sigue con la transferencia de datos de MongoDB a Elasticsearch, este proceso se lo realiza mediante el script de la imagen a continuación.

![image](https://user-images.githubusercontent.com/66692550/133805352-dceddf6d-a1cc-48eb-a8ec-1361da05a27c.png)

Siguiendo con la recolección y análisis de datos, se ha conseguido datos de la plataforma de YouTube, de la fuente botster.io, para el tema de noticias mundiales. 

![image](https://user-images.githubusercontent.com/66692550/133805457-67bcdd81-0c54-49d9-95bf-836288933b45.png)

Para que el análisis sea claro y las visualizaciones puedan ser óptimas, se procede a realizar la limpieza de datos. La limpieza de los datos se realiza en RapidMiner, muestra como es el proceso y que operadores se usan para realizar la purga de datos.

![image](https://user-images.githubusercontent.com/66692550/133805482-32aef241-87f6-4b83-92bb-e659215eb4f3.png)

Estos datos limpios pasan a una base de datos en MongoDB llamada “noticiasTelemundo”, dentro de una colección “noticias” se puede visualizar el conjunto de datos que se han recolectado. 

![image](https://user-images.githubusercontent.com/66692550/133805534-04a41ed1-81c7-4a73-a2ac-34caa0b3675b.png)

El proceso sigue con la transferencia de datos de MongoDB a Elasticsearch, este proceso se lo realiza mediante el script de la imagen a continuación.

![image](https://user-images.githubusercontent.com/66692550/133805600-86b12d98-5d1e-4604-88d3-e3b502ad796d.png)

### Noticias mundiales en Instagram 

Se realiza una búsqueda más para el tema de Noticias mundiales en la fuente Instagram, se hace uso de la misma herramienta, botster.io, para la obtención de datos. 

![image](https://user-images.githubusercontent.com/66692550/133805673-b7087a8a-64d4-42ee-8377-7bfe9c097a86.png)

Los datos recolectados pasan a ser almacenados en MySQL, en la base de datos “instagram” se importan todos los datos obtenidos de botster.io como se ve en la siguiente imagen.

![image](https://user-images.githubusercontent.com/66692550/133805701-837ece82-801f-489d-a8d8-ea7fcf779944.png)

El proceso sigue con la transferencia de datos de MongoDB a Elasticsearch, este proceso se lo realiza mediante el script de la imagen a continuación.

![image](https://user-images.githubusercontent.com/66692550/133805725-fd1b0fdb-db29-4a65-aa7d-e4c2280c8442.png)

Una vez finalizada la extracción de los datos se procede a enviarlos a unificarlos para poder realizar el análisis de los mismos.

## Análisis de los datos obtenidos

### Dashboard MIGRACION:

![image](https://user-images.githubusercontent.com/66692550/133806578-68c3d596-69f8-4453-b1ef-9d67d4ef5beb.png)

En el año 2020 la migración de ciudadanos ecuatorianos al país norte americano de Estados Unidos era más del 50%. Este suceso ocurre a raíz de la pandemia por Covid-19. La salida de ecuatorianos a países como Estados Unidos, una potencia mundial, ha arrojado un total de 52.69% de personas que han emigrado a América del norte. Por otro lado, el país que menos emigrantes ecuatorianos tiene es España con el menor porcentaje de 7.48% de ecuatorianos que han ido al país europeo. 
El segundo destino favorito para los ecuatorianos es Perú con un 20.24% de ecuatorianos emigrantes, sigue el país vecino, Colombia con un 9.79% y México que recibe un 9.25% de emigrantes ecuatorianos. 

![image](https://user-images.githubusercontent.com/66692550/133806633-6d004b52-79e6-4ed6-b18d-0e833229fb3c.png)

La migración de ecuatorianos en el año 2018 fue exponencial, son más de 3 millones de ciudadanos que han migrado de su país de origen. Se denota un decremento en picada de las entradas a países extranjeros en el año 2020. Si se visualiza en retrospectiva desde el año 2000, un año de crisis por el feriado bancario, se nota un incremento de la migración ecuatoriana hasta el año 2018. 

### Dashboard VIDEOJUEGOS:

![image](https://user-images.githubusercontent.com/66692550/133806681-dca510d5-1c4c-4b7b-928b-fec85a74fb0d.png)

En el tema de videojuegos la visualización indica que los juegos en plataformas como PlayStation 2 son los más vendidos mundialmente, al igual que en Europa se venden más videojuegos de la plataforma PlayStation 2. Se puede observar que los videojuegos que más se venden en Norte América son de consolas Xbox 360. Si nos dirigimos a oriente se puede encontrar que en Japón se venden juegos que son de consolas Nintendo DS. Por otro lados las demás ventas de juegos también se las lleva el PlayStation 2. Y por ultimo se ve que los juegos que menos se venden son de las consolas TurboGrafx-16.

![image](https://user-images.githubusercontent.com/66692550/133806716-aa6e36c1-62f5-49e1-ad18-1519ec5957c5.png)

Como se puede apreciar en el mapa, los estados Montana e Idaho prefieren el género de videojuego de carreras, el cual consiste en carreras, competencias, modificación de autos, etc. Además, se puede ver el promedio de dinero invertido por persona es de 236 Euros en este género de juego.

![image](https://user-images.githubusercontent.com/66692550/133806750-c2409515-b627-4072-b490-ca2f535be18c.png)

Con respecto a los estados de Oyaho y Pensilavania se tiene que prefieren el género de acción, con videojuegos que representen retos mentales, exploración de mundos, persecuciones, etc. El promedio de dinero invertido por persona en este género es alrededor de 519 Euros.

![image](https://user-images.githubusercontent.com/66692550/133806780-7b19b235-47d6-4536-b059-515fb41f5cd7.png)

La visualización anterior muestra que el estado de NuevaYork prefiere el género de videojuego de aventura, con una cifra de dinero invertido de 63 Euros por persona. Por lo que al ser un género bastante popular no recauda tanto dinero como en otros lugares.

![image](https://user-images.githubusercontent.com/66692550/133806826-3c7ff9b3-0b39-49d7-a6dc-dbfdd089f1a5.png)

Con respecto al estado de Kentucky, se puede evidenciar que el género de videojuego preferido por los jugadores es de tipo plataforma. Y ha recaudado una cifra aproximada de 200 euros invertidos por persona en videojuegos de aventura.

![image](https://user-images.githubusercontent.com/66692550/133806852-0504e7e1-a850-4d21-ad20-2089cf871bfd.png)

Por otra parte, en la zona del Caribe los jugadores se inclinan más por el género shooter, es decir videojuegos con temática de guerra y uso de armas. Junto a esto la media de dinero que las personas invierten en este tipo de videojuego es de 317 Euros.

![image](https://user-images.githubusercontent.com/66692550/133806905-b71891c7-dbd9-447c-b368-e2ac9e40d493.png)

En esta visualización es posible apreciar que en Polonia los videojuegos más jugados son los de rol, donde los jugadores con capaces de explorar mundo abiertos o semiabiertos dentro un juego. También, se determina que la media de dinero invertido por persona en este tipo de juego es de 188 Euros.

![image](https://user-images.githubusercontent.com/66692550/133806944-7e29647b-e814-4e3a-80b2-68832e944ecb.png)

Esta visualización explica que en Italia el género de videojuego deportes es el más jugado en ese país. Además, se puede observar la cantidad de dinero invertido en este género con una media de 376 euros por persona que lo juega.

### Dashboard NOTICIAS YOUTUBE

![image](https://user-images.githubusercontent.com/66692550/133806992-b110fdbc-b871-4ff0-a23a-c80620b68a4a.png)

El dashboard anterior representa la frecuencia de usuarios en YouTube que prefieren revisar un tipo de noticia. Por lo que, alrededor de 4 millones de personas prefieren visualizar noticias sobre “El ‘jefe de jefes’ rompe el silencio tras 32 años”. Los usuarios también optan por ver temas sobre entrevistas a famosos, la situación de su país, escándalos públicos, etc.

![image](https://user-images.githubusercontent.com/66692550/133807014-fa2cdf27-c435-4cbd-9506-d5cd24fa356e.png)

En esta visualización es posible observar que usuarios de YouTube prefieren ver videos sobre noticias de 5 minutos y 8 segundos. En cambio, esta tendencia tiene a ser menor con videos que duren entre 12minutos 58 segundos a 20min, por lo que la tasa de frecuencia de personas disminuye a medida que el video dura más minutos.

### Dashboard Noticias Instagram

![image](https://user-images.githubusercontent.com/66692550/133807313-4e73116d-5ca7-4567-b2aa-b37f5fa62114.png)

En la visualización anterior se puede apreciar que gran cantidad de usuarios de Instagram de 3 cuentas que ofrecen contenido noticias, prefieren ver temas sobre políticas, farándula, deportes, entretenimiento y gastronomía. En menor medida las personas prefieren ver noticias sobre México o compras de domicilios. 
