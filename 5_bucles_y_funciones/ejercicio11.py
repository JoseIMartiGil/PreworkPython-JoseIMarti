'''Define una función que tome una cadena y determine si es un palíndromo.'''
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

print(es_palindromo("Anita lava la tina")) 