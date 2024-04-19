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
df['otros_medios']=df['otros_medios'].fillna(6922148.759)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#En subtotal de alimentos y bebidas decidí rellenarlo con los valores no nulos hacía adelante. Ya que son 10 valores nulos y así pueden ser sustituidos con valores anteriores
df['subtotal_ventas_alimentos_bebidas'] =df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Para bebidas decidií llenarlo con promedio de la columna ya que solo falta un dato.
df['bebidas'] =df['bebidas'].fillna(round(df['bebidas'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Para alamcen decidí utilizar el backward fill para sustituir el dato faltante
df['almacen'] =df['almacen'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Panaderia tiene un dato nulo. No quiero sustituirlo con el promedio ni la mediana sino con un valor númerico (0). De esta manera ahora la venta de panaderia en el valor nulo se vuelve cero
df['panaderia'] =df['panaderia'].fillna(0)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Para lacteos también voy a sustituir el valor nulo con un cero, solo tiene 1 valor nulo la columna de lácteos
df['lacteos'] =df['lacteos'].fillna(0)
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Para carnes voy a sustituir el valor nulo de la columna con el valor central de los datos de la columna carnes. Por lo que voy a utilizar la mediana
df['carnes'] =df['carnes'].fillna(round(df['carnes'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Para verdureria y fruteria voy a utilizar un backward fill para sustituir los datos con los valores posteriores al dato nulo.
df['verduleria_fruteria'] =df['verduleria_fruteria'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Para alimentos preparados en rostiseria voy a utilizar un foward fill para sustituir valor faltante con el valor anterior.
df['alimentos_preparados_rotiseria'] =df['alimentos_preparados_rotiseria'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#En la columna de indumentaria clazado textiles hogar hay dos valores nulos, voy a sustituir los con el promedio de los otros valores en la columna.
df['indumentaria_calzado_textiles_hogar'] =df['indumentaria_calzado_textiles_hogar'].fillna(round(df['indumentaria_calzado_textiles_hogar'].mean(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Para electronicos artículos hogar utilizare la mediana para rellenar los datos faltantes y así utilizar el valor central y mantener las ventas dentro del rango de datos en el que se encuentran los demás valores de la columna
df['electronicos_articulos_hogar'] =df['electronicos_articulos_hogar'].fillna(round(df['electronicos_articulos_hogar'].median(),1))
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#Por último voy a utilizar el promedio para la columna se otros. Esta columna tiene 4 valores nulos por lo que decidí que el promedio es la mejor opción para que los datos nuevos sean coherentes con la información que ya tiene la columna.
df['otros'] =df['otros'].fillna(round(df['otros'].mean(),1))
valores_nulos=df.isnull().sum()
print(valores_nulos)


