from datetime import datetime

# Esta función crea el log.txt con la fecha y hora, la operación y el resultado.
def crear_registro(operacion, resultado):
    fecha_hora = datetime.now()  # Variable que contiene la fecha y hora
    fecha_hora = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")  # Se da formato a la fecha y hora.
    file = open("log.txt", "a")
    file.write(f"{fecha_hora}, {operacion}, {resultado}\n")
    file.close()