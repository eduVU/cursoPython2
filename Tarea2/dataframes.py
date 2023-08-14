import requests as req
import pandas as pd
import matplotlib.pyplot as plt

# Esta función hace un request tipo GET al API y una lista de diccionarios con información sobre API's públicas.
def llamarApi():
    url = "https://api.publicapis.org/entries"
    getResponse = req.get(url)

    if getResponse.status_code == 200:
        publicApis = getResponse.json()  # El resultado es un diccionario con dos entradas, la entrada "entries" contiene una lista de diccionarios con info de los APIs.
        return publicApis
    else:
        print("ERROR: No se ha podido realizar la solicitud.\n")

# Esta función reúne los datos del llamado al API y crea un DataFrame con la información obtenida.
def crear_data_frame():
    resultados = llamarApi()
    tablaAPI=pd.DataFrame(resultados['entries'])  # La entrada "entries" del resultado del API es la que contiene la info importante en forma de una lista de diccionarios.
    return tablaAPI

# Esta función manipula el DataFrame creado para obtener estadísticas de interés y representarlas gráficamente usando matplotlib.
def graficarEstadisticas():
    resultadosAPI = crear_data_frame()  # Se obtiene el DataFrame principal con la info del API request.

    # La primera estadística de interés es la cantidad de APIS de este sitio que utilizan HTTPS.
    apisSeguras = resultadosAPI["HTTPS"].value_counts()  # Muestra la cantidad de APIs que usan https (true) y las que usan http (false). 
    
    etiquetas = "HTTPS", "HTTP"  # Etiquetas del plot.
    explotar = (0.1, 0)  # Configuraciones estéticas del plot.
    apisSeguras.plot.pie(explode=explotar, labels=etiquetas, autopct='%1.1f%%')
    plt.xlabel("")  # Título del eje X.
    plt.ylabel("")  # Título del eje Y.
    plt.title("Distribución porcentual de las APIs públicas según su protocolo HTTP")  # Nombre del gráfico.
    plt.legend()  # Leyenda para identificar cada sector.
    plt.show()

    # La segunda estadística de interés es la cantidad de APIS que no necesitan ningún método de autenticación para ser usadas.
    apisNoAuth = resultadosAPI["Auth"].value_counts()  # Muestra los distintos métodos de autenticación para las APIs listadas. 

    fig, estadisticaAut = plt.subplots()
    nombresAuth= ["Ninguno", "apiKey", "OAuth", "X-Mashape-Key", "User-Agent"]  # Etiquetas del plot.
    valoresAuth = apisNoAuth.values  # Valores del DataFrame usados.
    coloresAuth = ["tab:red", "tab:blue", "tab:olive", "tab:orange", "tab:green"]
    estadisticaAut.bar(nombresAuth, valoresAuth, color=coloresAuth)
    estadisticaAut.set_ylabel('Cantidad')
    estadisticaAut.set_title("APIs públicas agrupadas por método de autenticación requerido")
    plt.show()

    # La tercera estadística de interés es la cantidad de APIs disponibles por categoría.
    categoriasApi = resultadosAPI["Category"].value_counts()  # Muestra la cantidad de APIs que usan https (true) y las que usan http (false). 

    fig, estadisticaCat = plt.subplots()
    nombresCat = categoriasApi.index
    valoresCat = categoriasApi.values  # Valores del DataFrame usados.
    estadisticaCat.barh(nombresCat, valoresCat)
    estadisticaCat.set_xlabel('Cantidad')
    estadisticaCat.set_title("APIs públicas agrupadas por categoría")
    plt.xticks(rotation = 90)  # Rotación para los valores del eje x.
    plt.show()   
    print("\n")