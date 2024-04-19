import pandas as pd
import numpy as np

#Carga desde un archivo .xlsx sin indice
df = pd.read_csv("ventas_totales.csv")

#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

#Quitar nulos

#Para salon ventas con 6 valores nulos decidí que lo mejor era rellenar esos valores nulos con el promedio de los otros valores de la columna. Esto debido a que son ventas y para mantener un promedio de lo que generalmente se vende en salon ventas
df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
valores_nulos = df.isnull().sum()
#print(valores_nulos)

#Para tarjeta de debito y de crédito decidí rellenar los valores nulos con la mediana. Esto para poder mantener las ventas con el valor central de los datos ya incluidos.
df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Para otros medios con un solo valor nulo decidí sustituir el valor nulo con un valor númerico. Este valor númerico lo obutve de datos ya en la columna. Decidí usar este método también para prácticar
