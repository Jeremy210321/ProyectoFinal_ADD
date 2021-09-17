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

response = requests.get('https://www.ecuadorencifras.gob.ec/entradas-y-salidas-internacionales/')
soup = BeautifulSoup(response.content, "lxml")

DatosTotales=[]
Ecuatorianos=[]
Extranjeros=[]
IndicesEcuatorianos=[4,7]
IndicesExtranjeros=[5,8]
Fecha=[2020,2020]

post_ecuatorianos=soup.find_all("td", style="text-align: center; color: #7c7c7b;")
post_extranjeros=soup.find_all("td", class_="numero")
    
for element in post_ecuatorianos:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    DatosTotales.append(limpio.strip())
    
for element in range(len(IndicesEcuatorianos)):
    Ecuatorianos.append(DatosTotales[IndicesEcuatorianos[element]])
    Extranjeros.append(DatosTotales[IndicesExtranjeros[element]])

#Guardar en un DataFrame

MigracionEcuaExtran=pd.DataFrame({'Fecha':Fecha,'Ecuatorianos':Ecuatorianos,'Extranjeros':Extranjeros}, index=['Entradas','Salidas'])

#Pasa el DataFrame hacia SQLite

MigracionEcuaExtran.to_sql('datosMigracionEcuExtran', conection)