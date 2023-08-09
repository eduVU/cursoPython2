import pandas as pd
import matplotlib.pyplot as plt

# Se crea un dataframe a partir de los datos del archivo CSV.
ventas = pd.read_csv("ventas.csv")

# Se crea la nueva columna "Ganancia" a partir de las columnas "Ventas" y "Gastos".
ventas["Ganancia"] = ventas["Ventas"] - ventas["Gastos"]
print(ventas)

# Se crea un gráfico de líneas con dos elementos: las ventas por mes y los gatos por mes.
plt.plot(ventas["Mes"].values, ventas["Ventas"].values, label="Ventas")  # Valores en x e y para la línea de ventas.
plt.plot(ventas["Mes"].values, ventas["Gastos"].values, label="Gastos")  # Valores en x e y para la línea de gastos.
plt.xlabel("Mes")  # Título del eje X.
plt.ylabel("Cantidad")  # Título del eje Y.
plt.title("Evolución mensual de las ventas y los gastos")  # Nombre del gráfico.
plt.legend()  # Leyenda para identificar cada línea.
plt.grid()  # Activar cuadrícula.
plt.show()