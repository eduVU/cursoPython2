import ids, time, requests
import threading, concurrent.futures

thread_local = threading.local()

# Esta función crea una sesión de requests local para threading en caso de que no exista una.
def crear_sesion():
    if not hasattr(thread_local, "sesion"):
        thread_local.sesion = requests.Session()
    return thread_local.sesion

# Versión modificada para threading de la función proporcionada con el enunciado del laboratorio.
def getOneUser(id):
    sesion = crear_sesion()  # Crea una sesión para threading.
    url = "https://jsonplaceholder.typicode.com/users/"
    with sesion.get(url) as response:
        return response.json()[id]

# Esta función hace el llamado al api usando la lista de ids dada e imprime solo el nombre de usuario.
# Versión ajustada a threading usando concurrent.futures.
def llamar_api(ids):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for id in ids:
            executor.datosUsuario = getOneUser(id)
            print(executor.datosUsuario.get("name"))

inicio = time.time()
llamar_api(ids.ids)
tiempoTotal = time.time() - inicio
print(f"La operación tardó {tiempoTotal} segundos.")
