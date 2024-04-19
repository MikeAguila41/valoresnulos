import pandas as pd
import numpy as np

#Carga desde un archivo .xlsx sin indice
df = pd.read_excel("devoluciones.xlsx")

#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

#Quitar nulos

#Para CVE_VEND voy a utilizar un backward fill para sustituir los datos con los valores posteriores al dato nulo porque solo varían entre 1-6.
df['CVE_VEND'] =df['CVE_VEND'].fillna(method='bfill')

#Para FECHA_CANCELA también voy a sustituir el valor nulo con un cero, ya que no hay valores en esa columna.
df['FECHA_CANCELA'] = df['FECHA_CANCELA'].fillna(0)

#Para CVE_PEDI voy a utilizar un backward fill para sustituir los datos con los valores posteriores al dato nulo.
df['CVE_PEDI'] =df['CVE_PEDI'].fillna(method='bfill')

#Para DOC_ANT voy a utilizar un backward fill para sustituir los datos con los valores posteriores al dato nulo.
df['DOC_ANT'] =df['DOC_ANT'].fillna(method='bfill')

valores_nulos = df.isnull().sum()
print(valores_nulos)

#Convertir DataFrame a CSV
df.to_excel('devoluciones_limpio.xlsx')