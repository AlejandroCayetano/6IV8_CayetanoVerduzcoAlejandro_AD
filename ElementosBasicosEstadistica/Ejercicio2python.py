import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Ahora cargamos los datos
df = pd.read_excel('ElementosBasicosEstadistica/Datos_Con_Sucursal.xlsx')

ventas_totales = df['ventas_tot'].sum()
print('Las ventas totales son: ', ventas_totales)
