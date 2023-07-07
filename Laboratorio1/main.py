import trigonometria as trig
import registros as reg

# Se crea un objeto de la clase Trig.
operaciones = trig.Trig()

while True:
  opcion = input("Ingrese la operación que desea realizar o ingrese 'salir' para salir:\n"
"1. sen(pi)\n"
"2. cos(pi)\n"          
"3. tan(pi)\n")

  # El programa termina cuando el usuario elige salir.
  if opcion.lower() == "salir": break
  # Creación de registros y presentación de resultados para las opciones disponibles.
  elif int(opcion) == 1:
    operacion = "sen(pi)"
    resultado = operaciones.calcular_sen_pi()
    print(f"El seno de pi es: {resultado}.\n")
    reg.crear_registro(operacion, resultado)
  elif int(opcion) == 2:
    operacion = "cos(pi)"
    resultado = operaciones.calcular_cos_pi()
    print(f"El coseno de pi es: {resultado}.\n")
    reg.crear_registro(operacion, resultado)
  elif int(opcion) == 3:
    operacion = "tan(pi)"
    resultado = operaciones.calcular_tan_pi()
    print(f"La tangente de pi es: {resultado}.\n")
    reg.crear_registro(operacion, resultado)