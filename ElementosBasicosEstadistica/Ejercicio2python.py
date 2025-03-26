import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Ahora cargamos los datos
df = pd.read_excel('ElementosBasicosEstadistica/Datos_Con_Sucursal.xlsx')

#1- Ventas totales
ventas_totales = df['ventas_tot'].sum()

#Imprimimos
print(f'Las ventas totales son: ${ventas_totales:,.2f}')

#2- Socios con y sin adeudo
socios_con_adeudo = df[df["B_adeudo"] == "Con adeudo"].shape[0]
socios_sin_adeudo = df[df["B_adeudo"] == "Sin adeudo"].shape[0]

#% de socios con y sin adeudo
total_socios = socios_con_adeudo + socios_sin_adeudo
porcentaje_con_adeudo = (socios_con_adeudo / total_socios) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / total_socios) * 100

#Imprimimos
print(f"Socios con Adeudo: {socios_con_adeudo:,}")
print(f"Socios sin Adeudo: {socios_sin_adeudo:,}")
print(f"Porcentaje de Socios con Adeudo: {porcentaje_con_adeudo:.2f}%")
print(f"Porcentaje de Socios sin Adeudo: {porcentaje_sin_adeudo:.2f}%")

# 3. Gráfica de ventas totales respecto del tiempo
plt.figure(figsize=(10, 5))
plt.bar(df["B_mes"].astype(str), df["ventas_tot"], color="#57B6EB")
plt.xticks(rotation=45)
plt.xlabel("Mes")
plt.ylabel("Ventas Totales")
plt.title("Ventas Totales Respecto al Tiempo")
plt.show()

# 4. Gráfica de desviación estándar de los pagos realizados respecto del tiempo
dsv_pagos = df.groupby("B_mes")["pagos_tot"].std()

plt.figure(figsize=(10, 5))
plt.plot(dsv_pagos.index.astype(str), dsv_pagos, marker="o", linestyle="-", color="#5AEB92")
plt.xticks(rotation=45)
plt.xlabel("Mes")
plt.ylabel("Desviación Estándar de Pagos")
plt.title("Desviación Estándar de Pagos Respecto al Tiempo")
plt.show()