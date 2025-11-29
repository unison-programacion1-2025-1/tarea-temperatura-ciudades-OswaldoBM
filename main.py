import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Ver tipos de datos de las columnas
print(df.dtypes)

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])
# Establecer la columna 'Date' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# TODO: Crear funcion para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):
    return kelvin-273.15
    

# TODO: Copiar el DataFrame original y nombralo df_celsius
df_celsius = df.copy()
# TODO: Convertir las temperaturas de cada ciudad de Kelvin a Celsius usando la funcion creada
df_celsius["Phoenix"] = df_celsius["Phoenix"].apply(kelvin_to_celsius)
# Analisis
i_minimo = df_celsius["Phoenix"].idxmin()
temperatura_minima = df_celsius["Phoenix"][i_minimo].round(2)
i_maximo = df_celsius["Phoenix"].idxmax()
temperatura_maxima = df_celsius["Phoenix"][i_maximo].round(2)
temperatura_promedio = df_celsius["Phoenix"].mean()

# TODO: Imprime que día y hora se registró la temperatura mínima en Phoenix con el siguiente mensaje: "El día con la temperatura mínima en Phoenix fue: {fecha}"
print(f"El día con la temperatura mínima en Phoenix fue: {i_minimo}")
# TODO: Imprime la temperatura mínima en Phoenix con el siguiente mensaje: "La temperatura mínima registrada en Phoenix fue de: ",temperatura," °C""
print(f"La temperatura mínima registrada en Phoenix fue de: {temperatura_minima} °C")

# TODO: Imprime que día y hora se registró la temperatura máxima en Phoenix con el siguiente mensaje: "El día con la temperatura máxima en Phoenix fue: {fecha}"
print(f"El día con la temperatura máxima en Phoenix fue: {i_maximo}")

# TODO: Imprime la temperatura máxima en Phoenix con el siguiente mensaje: "La temperatura máxima registrada en Phoenix fue de: ", temperatura, " °C""
print("La temperatura máxima registrada en Phoenix fue de: ",temperatura_maxima," °C")

# TODO: Imprime la temperatura promedio en Phoenix durante el año 2016 con el siguiente mensaje: "La temperatura promedio durante 2016 en Phoenix fue de: ", temperatura, " °C""
print("La temperatura promedio durante 2016 en Phoenix fue de: ",temperatura_promedio," °C")

# Graficar la temperatura de Phoenix durante el año 2016
plt.figure(figsize=(20, 10))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], label='Phoenix')
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV
df_celsius.to_csv("temperatura_celsius.csv")


