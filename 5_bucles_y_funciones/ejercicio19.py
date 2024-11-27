'Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.'
def tienen_elementos_comunes(lista1, lista2):
    return bool(set(lista1) & set(lista2))

print(tienen_elementos_comunes([1, 2, 3], [3, 4, 5]))