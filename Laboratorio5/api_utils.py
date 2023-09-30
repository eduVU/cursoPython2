import requests as req
import re
import pandas as pd
import matplotlib.pyplot as plt
import threading, concurrent.futures

thread_local = threading.local()

# Esta función crea una sesión de requests local para threading en caso de que no exista una.
def crear_sesion():
    if not hasattr(thread_local, "sesion"):
        thread_local.sesion = req.Session()
    return thread_local.sesion

# Esta función recibe un string con fecha en formato AAAA-MM-DD, filtra solo el año y lo devuelve como un entero.
def filtrar_fecha_lanzamiento(fecha):
    patronDeFecha = r"^\d{4}"  # Patrón de regex para obtener solo el año de la fecha ingresada.
    resultadoPatron = re.search(patronDeFecha, fecha)  # Se compara la fecha dada con el patrón de regex.
    return int(resultadoPatron.group())  # Se retorna el año como un entero.

# Esta función recibe un string con el título de la película, y comprueba si contiene la palabra "Action".
def filtrar_titulo(titulo):
    patronDeTitulo = r"\s*Action\s*"  # Patrón de regex para obtener solo las películas deseadas.
    return bool(re.search(patronDeTitulo, titulo))

# Esta función hace un llamado al API y obtiene la info disponible para una película según su ID.
def obtener_pelicula(id):
    sesion = crear_sesion()  # Crea una sesión para threading.
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key=b096f7e1a5e3291eb3b771afa219d33e"
    headers = {"accept": "application/json"}
    with sesion.get(url, headers=headers) as pelicula:
        return pelicula

# Esta función hace el llamado al API usando la lista de ids dada y guarda el título, calificación y fecha de lanzamiento para 
# cada película lanzada en el año 2000 o posterior.
def llamar_api(ids):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        peliculasValidas = {}  # Este diccionario contiene las películas lanzadas en el año 2000 o luego obtenidas del API.
        indice = 0  # Contador para el nombre de las entradas del diccionario.
        for i in range(ids):
            executor.pelicula = obtener_pelicula(i)  # Llama al API y obtiene la ficha de datos de la película con el id dado.
            if executor.pelicula.status_code == 200:
                anioLanzamiento = filtrar_fecha_lanzamiento(executor.pelicula.json()["release_date"])  # Filtra el año de lanzamiento de la película.
                chequeoTitulo = filtrar_titulo(executor.pelicula.json()["original_title"])  # Filtra el título de las películas que NO contengan "Action".
                if anioLanzamiento >= 2000 and chequeoTitulo == False: 
                    peliculasValidas[f"{indice}"] = {"Titulo": executor.pelicula.json()["original_title"],
                            "Calificación": executor.pelicula.json()["vote_average"],
                            "Fecha_de_lazamiento": executor.pelicula.json()["release_date"]}
                    indice = indice + 1
    return peliculasValidas

# Esta función reúne los datos del llamado al API y crea un DataFrame con la información obtenida.
def crear_data_frame(ids):
    listaPeliculas = llamar_api(ids)
    tablaPeliculas=pd.DataFrame(listaPeliculas)  # La entrada "entries" del resultado del API es la que contiene la info importante en forma de una lista de diccionarios.
    tablaTranspuesta = tablaPeliculas.T  # Transposición del dataframe para un manejo más sencillo del mismo.
    return tablaTranspuesta

# Esta función manipula el DataFrame creado para graficar las calificaciones de interés.
def graficarEstadisticas(ids):
    tablaPeliculas = crear_data_frame(ids)  # Se obtiene el DataFrame principal con la info del API request.

     # La estadística de interés es el conteo de películas para cada calificación registrada.
    conteoPeliculas = tablaPeliculas["Calificación"].value_counts()  # Realiza un conteo de películas para cada calificación disponible. 
    
    conteoPeliculas.plot(kind='bar',
                         title="Cantidad de películas por cada calificación registrada",
                         ylabel = "Cant. Películas")
    plt.show()
