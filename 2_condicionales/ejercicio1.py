'''Dado un número, imprime si es positivo o negativo.'''

numero = int(input("Ingresa un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")