'''Define una función que reciba una lista de números y retorne la suma acumulada de los números.'''
def suma_acumulada(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

print(suma_acumulada([1, 2, 3, 4, 5]))