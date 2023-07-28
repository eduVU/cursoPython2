import ids, time
import asyncio, aiohttp

# Versión modificada para asyncio de la función proporcionada con el enunciado del laboratorio.
async def getOneUser(sesion, id):
    url = "https://jsonplaceholder.typicode.com/users/"
    async with sesion.get(url) as response:
        resultado = response.json()[id]
        print(f"{resultado.get('name')}")
        
# Esta función hace el llamado al api usando la lista de ids dada e imprime solo el nombre de usuario.
# Versión ajustada a asyncio usando tareas.
async def llamar_api(ids):
    async with aiohttp.ClientSession() as sesion: # Crea una sesión para HTTP requests.
        tareas = []  # lista de tareas asíncronas.
        for id in ids:
            tarea = asyncio.ensure_future(getOneUser(sesion, id))
            tareas.append(tarea)
        await asyncio.gather(*tareas, return_exceptions=True)

inicio = time.time()
asyncio.get_event_loop().run_until_complete(llamar_api(ids.ids))
tiempoTotal = time.time() - inicio
print(f"La operación tardó {tiempoTotal} segundos.")
