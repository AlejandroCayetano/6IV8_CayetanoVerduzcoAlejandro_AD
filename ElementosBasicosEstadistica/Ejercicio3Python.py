"""Calcularemos las distancias entre todos los pares de puntos y determinaremos cuales están más alejados entre sí, y cuáles están más cercanos utilizando las distancias Euclidiana, Manhattan y Chebyshev"""

import numpy as np
import pandas  as pd
from scipy.spatial import distance

# Definimos las coordenadas de las tiendas
puntos = {
    'Punto A':(1,1),
    'Punto B':(1,5),
    'Punto C':(7,1),
    'Punto D':(3,3),
    'Punto E':(4,8),
    'Punto F':(8,2),
    'Punto G':(4,6),
    'Punto H':(2,1)
}

# Convertimos los puntos a un DataFrame
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X','Y']
print("Coordenadas de las tiendas: ")
print(df_puntos)

def calcular_distancias_euclidian(puntos):
    distancias = pd.DataFrame(index = df_puntos.index,columns = df_puntos.index)
    # Cálculo de distancias
    for i in df_puntos.index:
        for j in df_puntos.index:
            if i != j: # No calcula la distancia del mismo punto
                # Distancia Euclidiana
                distancias.loc[i,j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
    return distancias

def calcular_distancias_manhattan(puntos):
    distancias = pd.DataFrame(index=puntos.index, columns=puntos.index)
    for i in puntos.index:
        for j in puntos.index:
            if i != j: # No calcila la distancia del mismo punto
                # Distancia Euclidiana
                distancias.loc[i, j] = distance.cityblock(puntos.loc[i], puntos.loc[j])
    return distancias

def calcular_distancias_chebyshev(puntos):
    distancias = pd.DataFrame(index=puntos.index, columns=puntos.index)
    for i in puntos.index:
        for j in puntos.index:
            if i != j: # No calcila la distancia del mismo punto
                # Distancia Euclidiana
                distancias.loc[i, j] = distance.chebyshev(puntos.loc[i], puntos.loc[j])
    return distancias

distancias_euclidianas = calcular_distancias_euclidian(df_puntos)
distancias_manhattan = calcular_distancias_manhattan(df_puntos)
distancias_chebyshev = calcular_distancias_chebyshev(df_puntos)

valor_maximo = distancias_euclidianas.values.max()
(punto1,punto2) = distancias_euclidianas.stack().idxmax()

print(' \nTabla de Distancias Euclidianas:')
print(distancias_euclidianas)
print(' \nTabla de Distancias Manhattan:')
print(distancias_manhattan)
print(' \nTabla de Distancias Chebyshev:')
print(distancias_chebyshev)
print('Distancia Máxima: ', valor_maximo)
print('Entre el punto', punto1, 'y el punto', punto2)

# Otra manera
max_value = distancias_euclidianas.max().max()

# Obtener la columna que contiene el valor máximo
col_max = distancias_euclidianas.max().idxmax()

# Obtener el índice (fila) que contiene el valor máximo
id_max = distancias_euclidianas[col_max]

print(f"Valor máximo: {max_value}")
print(f"Columna: {col_max}")
print(f"Indice: {id_max}")