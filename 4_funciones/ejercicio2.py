'''Define una función que tome un número y retorne su factorial.'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n>0:
            return n * factorial(n - 1)
        else:
            return 'No es posible calcular el factorial para números negativos'

print(factorial(5))