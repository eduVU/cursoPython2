import requests as req

# Esta función hace un request tipo GET al API de chistes de Chuck y obtiene un chiste aleatorio.
def obtener_chiste_aleatorio():
    url = "https://api.chucknorris.io/jokes/random"
    getResponse = req.get(url)

    if getResponse.status_code == 200:
        chiste = getResponse.json()  # Diccionario con los valores del GET response.
        print("\n" + "Chiste obtenido:")
        print(chiste.get("value") +"\n")  # Del diccionario obtenido, se muestra solo el key que contiene al chiste.
    else:
        print("ERROR: No se ha podido realizar la solicitud.\n")

# Esta función hace un request tipo GET al API de chistes de Chuck y obtiene la lista de categorías de chistes disponibles.
def obtener_categorias():
    url = "https://api.chucknorris.io/jokes/categories"
    getResponse = req.get(url)

    if getResponse.status_code == 200:
        categorias = getResponse.json()  # Lista con los valores del GET response.
        print("\n" + "Categorías disponibles:")
        for item in categorias:
            print(item)
        print()
    else:
        print("ERROR: No se ha podido realizar la solicitud.\n")

# Esta función hace un request tipo GET al API de chistes de Chuck y obtiene un chiste aleatorio para una categoría dada.
def obtener_chiste_cat(categoria):
    url = f"https://api.chucknorris.io/jokes/random?category={categoria}"
    getResponse = req.get(url)

    if getResponse.status_code == 200:
        chiste = getResponse.json()  # Diccionario con los valores del GET response.
        print("\n" + "Chiste obtenido:")
        print(chiste.get("value") + "\n")  # Del diccionario obtenido, se muestra solo el key que contiene el chiste.
    else:
        print("ERROR: No se ha podido realizar la solicitud. Verifique que se haya escogido una categoría válida.\n")


# El menú principal corre en un bucle infinito, solo lo puede interrumpir el usuario.
while True:
    opcion = input("Elija una opción: \n"
          "1. Obtener un chiste de Chuck Norris aleatorio.\n"
          "2. Mostrar la lista de categorías disponibles.\n"
          "3. Elegir un chiste de una categoría específica.\n"
          "4. Salir.\n")

    if opcion == "1":
        obtener_chiste_aleatorio()
    elif opcion == "2":
        obtener_categorias()
    elif opcion == "3":
        categoria = input("Ingrese la categoría deseada: ")
        obtener_chiste_cat(categoria)
    elif opcion == "4":
        print("¡Adiós!")
        break
    else:
        print("ERROR: Ingrese una opción válida del menú.\n")
