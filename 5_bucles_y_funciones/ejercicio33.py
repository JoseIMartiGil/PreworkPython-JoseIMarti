'''Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.'''
def ordenar_por_ultimo(lista):
    return sorted(lista, key=lambda x: x[-1])

print(ordenar_por_ultimo([(1, 3), (3, 2), (2, 1)]))