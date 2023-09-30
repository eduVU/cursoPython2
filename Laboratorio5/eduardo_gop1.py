# Problema 1:
precio_original = float(input("Ingrese el precio original del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
descuento = precio_original * porcentaje_descuento / 100
precio_final = precio_original - descuento
print("El precio final con descuento es: ", precio_final)

# Problema 2:
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))
nota5 = float(input("Ingrese la quinta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("El promedio es :", promedio)

# Problema 3:
radio = float(input('Ingrese el radio del circulo: '))
pi = 3.14
area = pi*(radio**2)
print('El area del circulo es:',area)