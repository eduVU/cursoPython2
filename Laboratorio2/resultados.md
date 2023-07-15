## Presentación de resultados del Laboratorio 2.

Explicación:

Primero, dado que el código hace un llamado a un API y consigue información de una base de datos externa, es posible concluir que el problema en este caso es *afectado por I/O*. Por lo tanto, las dos opciones disponibles para mejorar el script usando concurrencia son **asyncio** y **threading**.

Para elegir la mejor opción posible, se implementaron soluciones usando ambos métodos de concurrencia y se comparó el tiempo de respuesta de cada uno con respecto al script original.

Script original:
- Nombre del archivo: main.py
- Método de concurrencia utilizado: ninguno.
- Duración total del programa: 37.16513919830322 segundos

Script con threading:
- Nombre del archivo: main_threading.py
- Método de concurrencia utilizado: threading.
- Duración total del programa: 10.519116878509521 segundos

Script con asyncio:
- Nombre del archivo: main_async.py
- Método de concurrencia utilizado: asyncio.
- Duración total del programa: No se logró llegar a un resultado concluyente.

Desafortunadamente, no logré implementar una solución correcta utilizando asyncio, de modo que no pude utilizar datos para la comparación. En teoría, asyncio debería de ser superior en velocidad de respuesta al método de threading y debería ser el método predilecto para implementar una solución a este problema.

Método elegido: threading, dado que no se pudo obtener resultados con el método de asyncio.