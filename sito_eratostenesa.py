import random

def sito_eratostenesa(n):
    if n < 2:
        return []

    sito = [True] * (n + 1)
    sito[0] = sito[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sito[i]:
            for j in range(i*i, n + 1, i):
                sito[j] = False

    return [i for i, is_prime in enumerate(sito) if is_prime]

# 3 liczby z przedziału 2–100
wylosowane_liczby = [random.randint(2, 100) for _ in range(3)]

# wyniki
for liczba in wylosowane_liczby:
    liczby_pierwsze = sito_eratostenesa(liczba)
    print(f"\nLiczby pierwsze do {liczba}:")
    print(liczby_pierwsze)


