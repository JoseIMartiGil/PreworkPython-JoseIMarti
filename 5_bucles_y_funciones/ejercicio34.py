'''Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.'''
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cadena if letra in vocales)

print(contar_vocales("Hola Mundo")) 