'''Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada carácter en la cadena.'''
def contar_caracteres(cadena):
    return {c: cadena.count(c) for c in set(cadena)}

print(contar_caracteres("hola mundo. Soy tu primer bug, TIEEEEMBLAAAAA"))