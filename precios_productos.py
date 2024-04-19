import pandas as pd
import numpy as np

#Carga desde un archivo .xlsx sin indice
df = pd.read_excel("precios_productos.xlsx")

#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

#Quitar nulos

#Para NOMBRE_VENDEDOR voy a sustituir el valor nulo con un cero, ya que no es una columna numérica y no podemos aplicar algún método
df['NOMBRE_VENDEDOR'] = df['NOMBRE_VENDEDOR'].fillna(0)

valores_nulos = df.isnull().sum()
print(valores_nulos)

#Convertir DataFrame a CSV
df.to_excel('precios_productos_limpio.xlsx')