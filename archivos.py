# Abrir un archivo en modo lectura
archivo = open("ejemplo.txt", "r")

contenido = archivo.read()

print(contenido)
archivo.close()

# Escribir en un archivo
archivo = open("ejemplo2.txt", "w")

archivo.write("Hola, Mundo!!")
archivo.close() # Siempre cerrar el archivo para liberar recursos

# Anadir contenido al archivo
archivo = open("ejemplo.txt", "a")
archivo.write("\nAdios, mundo")
archivo.close()

#Leer por línea
archivo = open("ejemplo.txt", "r")

for linea in archivo:
    print(linea.strip())
archivo.close()

# Escritura de varias lineas en un string en el archivo
lineas = ["Linea 1\n", "Linea 2\n", "Linea 3\n"]
archivo = open("escritura_multiple.txt", "w")
archivo.writelines(lineas)
archivo.close() # No olvidar cerrar el archivo

# Manejo de excepciones
try:
    with open("archivo_inexistente.txt", "r"):
        contenido = archivo.read()
        print()
except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print(f"Ocurrio un error: {e}")