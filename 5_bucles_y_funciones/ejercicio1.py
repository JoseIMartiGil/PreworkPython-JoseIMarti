'''Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.'''
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

fibonacci(10) 