'''Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.'''
def segundo_mas_grande(lista):
    return sorted(set(lista))[-2]

print(segundo_mas_grande([1, 2, 3, 4, 5]))