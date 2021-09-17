#Instalación de librerías

pip install pandas
pip install pysqlite3

#Librerias y funciones para WebScraping

import requests
from bs4 import BeautifulSoup
import pandas as pd
from bson.raw_bson import RawBSONDocument

    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))

#Librería y constante para conexión con SQLite

import sqlite3
conection = sqlite3.connect("database.db")

#WebScraping de un sitio web específico

response = requests.get('https://datosmacro.expansion.com/demografia/migracion/emigracion/ecuador')
soup = BeautifulSoup(response.content, "lxml")

Fecha=[]
Numeros=[]
Hombres=[]
Mujeres=[]
IndicesHombres=[0,4,8,12,16,20,24,28]
IndicesMujeres=[1,5,9,13,17,21,25,29]

post_fecha=soup.find_all("td", class_="fecha")
post_numeros=soup.find_all("td", class_="numero")
    
for element in post_fecha:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Fecha.append(limpio.strip())

for element in post_numeros:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Numeros.append(limpio.strip())
    
for element in range(len(IndicesMujeres)):
    Mujeres.append(Numeros[IndicesMujeres[element]])
    Hombres.append(Numeros[IndicesHombres[element]])

Datos=[]
def listado():
    i=0
    for n in range(len(Fecha)):
        Datos.append("Periodo " + str(i))
        i=i+1 
        
listado()

#Guardar en un DataFrame
MigracionHombresMujeres=pd.DataFrame({'Hombres Migrantes':Hombres,'Mujeres Migrantes':Mujeres}, index=Fecha)

#Pasa el DataFrame hacia SQLite
MigracionHombresMujeres.to_sql('datosMigracion_HyM', conection)