'''Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario.'''
def es_numero_perfecto(n):
    divisores = [i for i in range(1, n) if n % i == 0]
    return sum(divisores) == n

print(es_numero_perfecto(6))