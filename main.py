#Traer un registro de N ventas para analizar con pandas
#Primeros pasos con pandas

from data.listasSimuladas import generar_ventas
import pandas as pd

datos_simulados=generar_ventas(1000)

#Organizando la fuente de datos con pandas
tablaOrdenada=pd.DataFrame(datos_simulados)

#1. Obtener la informacion general de la fuente de datos
#print(tablaOrdenada.info())

#2. Obtener la informacion estadistica basica (descriptiva) de la fuente de datos
#print(tablaOrdenada.describe())

#3. Obtener la informacion de los primeros N registros de la fuente de datos
#print(tablaOrdenada.head(20))

#4. Obtener la informacion de los ultimos N registros de la fuente de datos
#print(tablaOrdenada.tail(20))

#5. Acceder a una columna (Seleccionar) en especifico
#print(tablaOrdenada["vendedor"])

#6. TAREA como hago para acceder a varias columnas al mismo tiempo

#7. PUEDO APLICAR AGRUPACIONES (AGRUPAR DATOS NUMERICOS Y STRING)
#print(tablaOrdenada.groupby("producto")["total"].sum())
#print(tablaOrdenada.groupby("vendedor")["total"].sum())
#print(tablaOrdenada.groupby("fecha")["total"].sum().head(31))