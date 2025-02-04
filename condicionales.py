# Condicionales: Nos permite ejecutar el código en base a condiciones
edad = int(input('Ingresa tu edad: '))

#if edad <= 18:
#    if edad > 59:
#        print('Eres un adulto mayor')
#    else:
#        print('Eres mayor de edad')
#else:
#    print('No pasas. Eres menor.')

nota = int(input('Ingresa la nota del estudiante: '))

if nota >= 90:
    print('Excelente')
elif nota >= 90:
    print('Muy bien')
elif nota >= 70:
    print('Bien')
else:
    print('Necesitas mejorar un poco')

condicion = 'no'
condicion = input('Desea salir del programa? (si/no)')

while not ( condicion != 'no'):
    nota = int(input('Ingresa la nota del estudiante: '))
    if nota >= 90:
        print('Excelente')
    elif nota >= 90:
        print('Muy bien')
    elif nota >= 70:
        print('Bien')
    else:
        print('Necesitas mejorar un poco')

    condicion = input('Desea salir del programa? (si/no)')