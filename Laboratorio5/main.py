import time
import api_utils

ids = 500  # La máxima id hasta la cual se consulta en el API.

inicio = time.time()
api_utils.graficarEstadisticas(ids)
tiempo = time.time() - inicio
print(f"Duración del proceso: {tiempo} s")

# Para 500 ids --> ~31.703717947006226 s
