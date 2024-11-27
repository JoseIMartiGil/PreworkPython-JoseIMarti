'''Define una función que tome un número y calcule su serie de Fibonacci.'''
def fibonacci_lista(n):
    a, b = 0, 1
    resultado = []
    for _ in range(n):
        resultado.append(a)
        a, b = b, a + b
    return resultado

print(fibonacci_lista(10))