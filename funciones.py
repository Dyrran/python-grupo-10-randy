# Recursividad
# 1. Caso base: Condición que retiene la recursividad.
# 2. Caso recursivo.

# n! - Factorial. Producto de los enteros positivos desde 1 hasta n.
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# Solucion iterativa
def factorial_iterativo(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(result)
    print(f"{result}")

# factorial_iterativo(5)

def factorial_recursivo(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    else:
        return n * factorial_recursivo(n - 1)
    
print(factorial_recursivo(5))
print(factorial_iterativo(5))