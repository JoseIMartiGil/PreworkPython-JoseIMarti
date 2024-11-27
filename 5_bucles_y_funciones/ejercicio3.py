'''Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.'''
def elementos_unicos(lista):
    return list(set(lista))#set, excluye duplicados

print(elementos_unicos([1, 2, 2, 3, 4, 4, 5]))