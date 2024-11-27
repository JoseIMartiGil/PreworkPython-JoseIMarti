'''Define una función que encuentre el elemento más común en una lista.'''
def elemento_mas_comun(lista):
    # Crear un diccionario para contar las frecuencias
    frecuencias = {}
    
    # Contar cada elemento en la lista
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    
    # Encontrar el elemento con la mayor frecuencia
    mas_comun = None
    max_frecuencia = 0
    for elemento, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            mas_comun = elemento
            max_frecuencia = frecuencia
    
    return mas_comun

print(elemento_mas_comun([1, 2, 2, 3, 3, 3, 4]))