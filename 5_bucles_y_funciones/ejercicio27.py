'''Define una función que tome una lista y retorne la lista sin duplicados.'''
def eliminar_duplicados(lista):
    return list(set(lista))

print(eliminar_duplicados([1, 2, 2, 3, 4, 4, 5]))