import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

#Mostrar las primeras 5 filas
print(df.head())

#Mostrar las ultimas 5 filas
print(df.tail())

#Mostrar una fila en especifico
print(df.iloc[7])

#Mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#Obtener la media de la columna total_rooms
mediadecuarto = df["total_rooms"].mean()
print('La media de total room es: ', mediadecuarto)

#Mediana
medianacuarto = df['median_house_value'].median()
print('La mediana de la columna valor mediana de la casa es: ', medianacuarto)

#La suma de popular
salario = df['population'].sum()
print('El salario total es de: ', salario)

#Para poder filtrar
vamosahacerunfiltro = df[df['ocean_proximity'] == 'ISLAND']
print(vamosahacerunfiltro)

#Vamos a hacer un grafico de dispersion
plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])
#Nombramos los ejes
plt.xlabel("Proximidad")
plt.ylabel("precio")

plt.title("Grafico de Dispersion de Proximidad al Oceano vs Precio")
plt.show()