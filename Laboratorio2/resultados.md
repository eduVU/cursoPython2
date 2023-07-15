Método elegido: asyncio

Explicación:

- Primero, dado que el código hace un llamado a un API y consigue información de una base de datos externa, es posible concluir que el problema en este caso es *afectado por I/O*. Por lo tanto, las dos opciones disponibles para mejorar el script usando concurrencia son **asyncio** y **threading**.

- Para elegir la mejor opción posible, se implementaron soluciones usando ambos métodos de concurrencia y se comparó el tiempo de respuesta de cada uno con respecto al script original.

Script original:
- Nombre del archivo: main.py
- Método de concurrencia utilizado: ninguno.
- Duración total del programa: 37.16513919830322 segundos

Script con asyncio:
- Nombre del archivo: main_async.py
- Método de concurrencia utilizado: asyncio.
- Duración total del programa: 

Script con threading:
- Nombre del archivo: main_threading.py
- Método de concurrencia utilizado: threading.
- Duración total del programa: 10.519116878509521 segundos