'''Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.'''

def contar_mayusculas_minusculas(cadena):
    mayusculas = sum(1 for c in cadena if c.isupper())
    minusculas = sum(1 for c in cadena if c.islower())
    return mayusculas, minusculas

print(contar_mayusculas_minusculas("Hola Mundo"))