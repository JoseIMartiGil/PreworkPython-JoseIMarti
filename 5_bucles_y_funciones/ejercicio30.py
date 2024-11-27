'''Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.'''
def cadena_mas_larga(lista):
    return max(lista, key=len)

print(cadena_mas_larga(["Patatas", "Hola Mundo", "Python"])) 