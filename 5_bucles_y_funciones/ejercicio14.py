'''Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.'''

def palabras_mas_largas(lista, n):
    return [palabra for palabra in lista if len(palabra) > n]

print(palabras_mas_largas(["Hola", "Mundo", "Python"], 4))