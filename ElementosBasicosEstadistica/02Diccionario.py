import pandas as pd

#Escribir una función que reciba un diccionario con las notas de los estudiantes del curso y desuelve una serie con minimo, maximo, media, desviacion tipica

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media','Desviación Estandar'])
    return estadisticas

notas = {'Juan': 9, 'Juanita': 7, 'Sandra':6.6, 'Fabian': 8.5,'Maximiliano': 7.5, 'Yamil': 9.8, 'Rosario': 9}
print(estadistica_notas(notas))