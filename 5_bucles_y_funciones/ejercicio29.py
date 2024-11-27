'''Define una función que reciba una lista de números y retorne el promedio de los números en la lista.'''
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

print(promedio([1, 2.1, 3, 4, 4.1])) 