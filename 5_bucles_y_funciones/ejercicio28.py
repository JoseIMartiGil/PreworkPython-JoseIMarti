'''Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.'''

def suma_cuadrados_pares(n):
    return sum(i ** 2 for i in range(2, n + 1, 2))

print(suma_cuadrados_pares(7)) 
