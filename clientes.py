import pandas as pd
import numpy as np

#Carga desde un archivo .xlsx sin indice
df = pd.read_excel("clientes.xlsx")

#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

#Quitar nulos

#Para RFC voy a sustituir el valor nulo con un cero, ya que no es una columna numérica y no podemos aplicar algún método
df['RFC'] = df['RFC'].fillna(0)
valores_nulos = df.isnull().sum()

#Para NOMBRE también voy a sustituir el valor nulo con un cero, ya que no es una columna numérica y no podemos aplicar algún método
df['NOMBRE'] = df['NOMBRE'].fillna(0)
valores_nulos = df.isnull().sum()

print(valores_nulos)
