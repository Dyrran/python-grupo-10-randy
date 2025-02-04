frutas = ['manzana', 'pera', 'uva', 'sandia', 'melon']

for fruta in frutas:
    print(fruta)



# limite = int(input('Ingrese el limite del rango: '))
# for i in range(limite):
#     print("Numero: ", i+1)

# for i in range(limite):
#     if i == 5:
#         continue
#     print("Numero con continue", i+1)



# Bucles anidados o matrices
# filas = int(input('Ingrese el numero de filas: '))
# columnas = int(input("Ingrese el numero de columnas: "))

# for i in range(filas):
#     for j in range(columnas):
#         print("Fila: ", i+1, "Columna: ", j+1)



# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]

# Imprime todos los items en la matriz sin importar la longitud de las listas internas
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print('Fila: ', i, 'Columna: ', j, ' Valor: ',matriz[i][j])

# Imprimir los valores en diagonal: 1, 5, 9.
# for i in range(3):
#     for j in range(3):
#         if (i==j):
#             print(matriz[i][j])

# Imprimir los valores en diagonal (simplificado)
# for i in range(len(matriz)):
#     print(matriz[i][i])



listaDeUsuarios = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'Maria', 'edad': 30},
    {'nombre': 'Pedro', 'edad': 35},
    {'nombre': 'Ana', 'edad': 40}
]

for usuario in listaDeUsuarios:
    print('Nombre ', usuario.get('nombre', 'No existe esta propiedad'), ' Edad: ', usuario['edad'])
