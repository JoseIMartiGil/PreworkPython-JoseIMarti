'''Define una función que tome un número y determine si es primo.'''
def es_primo(n):
    if n>0:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return "Por favor, usa un número no negativo"

print(es_primo(19))