'''Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.'''
def primeros_n_primos(n):
    primos = []
    candidato = 2
    while len(primos) < n:
        if all(candidato % p != 0 for p in primos):
            primos.append(candidato)
        candidato += 1
    return primos

print(primeros_n_primos(10)) 