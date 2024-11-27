'''Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.'''
def tabla_multiplicar(n):
    return {i: n * i for i in range(1, 11)}

print(tabla_multiplicar(5)) 