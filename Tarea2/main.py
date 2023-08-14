import dataframes as dt

# El menú principal corre en un bucle infinito, solo lo puede interrumpir el usuario.
while True:
    opcion = input("Elija una opción: \n"
          "1. Información general sobre los datos mostrados.\n"
          "2. Mostrar visualizaciones de los datos.\n"
          "3. Salir.\n")

    if opcion == "1":
        print("Este programa muestra información sobre un API que contiene un listado con cientos de APIs públicas (fuente: 'https://api.publicapis.org/entries').\n"
              "Los datos mostrados por este programa son los siguientes:\n"
              "- Figura 1: Es una gráfica circular que muestra la cantidad de APIs que utilizan una conexión segura, presentada porcentualmente.\n"
              "            La figura realiza una comparación de la cantidad de APIs que usan el protocolo HTTPS versus aquellas que usan el protocolo HTTP.\n"
              "- Figura 2: Es una gráfica de barras que muestra los distintos métodos de autenticación que se usan en las APIs y cuántas de ellas utilizan cada método.\n"
              "- Figura 3: Es una gráfica de barras horizontal que muestra todas las categorías disponibles y cuántas APIs hay para cada una de ellas.\n"
              )
    elif opcion == "2":
        dt.graficarEstadisticas()
    elif opcion == "3":
        print("¡Adiós!\n")
        break
    else:
        print("ERROR: Ingrese una opción válida del menú.\n")
