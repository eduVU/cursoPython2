import api
import ids
import time

# Esta función hace el llamado al api usando la lista de ids dada e imprime solo el nombre de usuario.
def llamar_api(ids):
    for id in ids:
        datosUsuario = api.getOneUser(id)
        print(datosUsuario.get("name"))

inicio = time.time()
llamar_api(ids.ids)
tiempoTotal = time.time() - inicio
print(f"La operación tardó {tiempoTotal} segundos.")
