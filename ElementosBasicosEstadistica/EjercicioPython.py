import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

# Medidas
rango = df["median_house_value"].max() - df["median_house_value"].min()
media = df["median_house_value"].mean()
mediana = df["median_house_value"].median()
moda = df["median_house_value"].mode()[0]
varianza = df["median_house_value"].var()
desv = df["median_house_value"].std()

# Tabla con los datos separados
estadisticas = pd.DataFrame({
    "Medida": ["Rango", "Media", "Mediana", "Moda", "Varianza", "Desviación Estándar"],
    "Valor": [rango, media, mediana, moda, varianza, desv]
})
estadisticas['Valor'] = estadisticas['Valor'].apply(lambda x: f"{x:,.2f}")
print(estadisticas.to_string(index=False))

# Histograma
plt.figure(figsize=(10, 5))
plt.hist(df['median_house_value'], bins=30, alpha=0.5, label='Median House Value', color='blue')
plt.hist(df['total_bedrooms'], bins=30, alpha=0.5, label='Total Bedrooms', color='red')
plt.hist(df['population'], bins=30, alpha=0.5, label='Population', color='green')

# Nombramos ejes
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Histograma Comparativo")
plt.legend()
plt.show()
