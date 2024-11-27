'''Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.'''

def elementos_diferentes(lista1, lista2):
    return list(set(lista1) ^ set(lista2))

print(elementos_diferentes([1, 2, 3], [3, 4, 5])) 