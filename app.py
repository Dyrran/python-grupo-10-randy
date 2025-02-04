# 1

def cb_amigo():
    return "habla menor"

def cb_ayuda():
    return "hey ayuda"

def cb_comer():
    return "tengo hambre"

def mensaje(fn_a, fn_b):
    return [fn_a(), fn_b()]

ct = mensaje(cb_amigo, cb_comer)
print(ct)

# 2

def caja_de_zapato(zapato):
    print(f"¿Viste que es bonito este zapato marca {zapato}?")
    return zapato

zapato = caja_de_zapato("nike")
print(f"prueba este {zapato}")

# 3

def cb_restar(a,b):
    return a-b

def cb_sumar(a,b):
    return a+b

def calcular(fn, x, y):
    return fn(x,y)

c_1 = calcular(cb_sumar, 20, 10)
c_2 = calcular(cb_restar, 20, 10)
print(c_1, c_2)

def calcular_avz(cb_a, cb_b, x, y, z, t):
    return [ cb_a(x,y), cb_b(z,t) ]

c = calcular_avz(cb_restar, cb_sumar, 10, 5, 5, 5)
print(c)