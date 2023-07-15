import ids, time, requests
import asyncio, aiohttp

# Versión modificada para asyncio de la función proporcionada con el enunciado del laboratorio.
def getOneUser(id):
    sesion = aiohttp.ClientSession()  # Crea una sesión para HTTP requests.
    url = "https://jsonplaceholder.typicode.com/users/"
    with sesion.get(url) as response:
        return response.json()[id]

# Esta función hace el llamado al api usando la lista de ids dada e imprime solo el nombre de usuario.
# Versión ajustada a asyncio usando tareas.
def llamar_api(ids):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    tareas = []  # lista de tareas asíncronas.
        for id in ids:
            executor.datosUsuario = getOneUser(id)
            print(executor.datosUsuario.get("name"))

inicio = time.time()
# asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
tiempoTotal = time.time() - inicio
print(f"La operación tardó {tiempoTotal} segundos.")
