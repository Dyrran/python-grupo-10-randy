# Características de una variable:
# 1. Nombre: Su identificador en el código
# 2. Valor: Sea un número, cadena de texto, fecha, etc.
# 3. Tipo de dato: Si puede ser número o cadena de texto, etc.
# 4. Ámbito: Local o global.

edad = "32"
nombre = "Sergio"
real = 3.14
booleano = True
lista = [1, 2, 3, 'Adrian', 'Sergio', 3.14, True, False]
tupla = (1, 2, 3)
diccionario = {"nombre": "Sergio", "edad": 32}
edad = 567

print(edad)
edad = 568
print(edad)

print(nombre)
print(real)
print(booleano)
print(lista)
print(tupla)
print(diccionario)

print('Variable edad', type(edad))
print('Variable real', type(nombre))
print(type(real))
print(type(booleano))
print(type(lista))
print(type(tupla))
print(type(diccionario))