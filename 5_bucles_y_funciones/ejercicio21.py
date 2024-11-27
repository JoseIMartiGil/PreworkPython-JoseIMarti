'''Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.'''
def contar_digitos_y_letras(cadena):
    digitos = sum(1 for c in cadena if c.isdigit())
    letras = sum(1 for c in cadena if c.isalpha())
    return digitos, letras

print(contar_digitos_y_letras("Hola123"))