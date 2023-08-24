import requests as req
import re
import time

# Esta función recibe un string con fecha en formato AAAA-MM-DD, filtra solo el año y lo devuelve como un entero.
def filtrar_fecha_lanzamiento(fecha):
    patronDeFecha = r"^\d{4}"  # Patrón de regex para obtener solo el año de la fecha ingresada.
    resultadoPatron = re.search(patronDeFecha, fecha)  # Se compara la fecha dada con el patrón de regex.
    return int(resultadoPatron.group())  # Se retorna el año como un entero.

# Esta función recibe un string con el título de la película, y comprueba si contiene la palabra "Action".
def filtrar_titulo(titulo):
    patronDeTitulo = r"\s*Action\s*"  # Patrón de regex para obtener solo las películas deseadas.
    resultadoPatron = re.search(patronDeTitulo, titulo)  # Se compara el título dado con el patrón de regex.
    if resultadoPatron:
        print(titulo)
        return True

# Esta función hace un llamado al API y obtiene la info disponible para una película según su ID.
def obtener_pelicula(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key=b096f7e1a5e3291eb3b771afa219d33e"
    headers = {"accept": "application/json"}
    pelicula = req.get(url, headers=headers)
    return pelicula

# Esta función hace el llamado al API usando la lista de ids dada y guarda el título, calificación y fecha de lanzamiento para 
# cada película lanzada en el año 2000 o posterior.
def llamar_api(ids):
    peliculasValidas = {}  # Este diccionario contiene las películas lanzadas en el año 2000 o luego obtenidas del API.
    indice = 0  # Contador para el nombre de las entradas del diccionario.
    for i in range(ids + 1):
        pelicula = obtener_pelicula(i)  # Llama al API y obtiene la ficha de datos de la película con el id dado.
        if pelicula.status_code == 200:
            anioLanzamiento = filtrar_fecha_lanzamiento(pelicula.json()["release_date"])  # Filtra el año de lanzamiento de la película.
            chequeoTitulo = filtrar_titulo(pelicula.json()["original_title"])  # Filtra el título de las películas que contengan "Action".
            if anioLanzamiento >= 2000 and chequeoTitulo == False: 
                peliculasValidas[f"{indice}"] = {"Titulo": pelicula.json()["original_title"],
                           "Calificación": pelicula.json()["vote_average"],
                           "Fecha_de_lazamiento": pelicula.json()["release_date"]}
                indice = indice + 1
    return peliculasValidas             

ids = 20 # La máxima id hasta la cual se consulta en el API.
inicio = time.time()
peliculas = llamar_api(ids)
print(peliculas)
tiempo = time.time() - inicio
print(f"Duración: {tiempo} s")

# TO DO:
# Retornar el diccionario anidado y crear un dataframe a partir del mismo
# Implementar threading en la parte del consumo de API (Lab 2) para bajar los tiempos.