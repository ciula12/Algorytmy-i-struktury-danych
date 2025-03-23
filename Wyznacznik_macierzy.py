import random

def wyznacznik(macierz):
    # Dla 1x1
    if len(macierz) == 1:
        return macierz[0][0]

    # Dla 2x2
    if len(macierz) == 2:
        return macierz[0][0] * macierz[1][1] - macierz[0][1] * macierz[1][0]

    # Inne
    det = 0
    for i in range(len(macierz)):
       
        minor = [wiersz[:i] + wiersz[i+1:] for wiersz in macierz[1:]]
        
        det += (-1) ** i * macierz[0][i] * wyznacznik(minor)
    
    return det

# Generowanie losowej macierzy n×n
n = random.randint(1, 5)
macierz = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

# Wyświetlenie macierzy
print("Losowa macierz:")
for wiersz in macierz:
    print(wiersz)

# Obliczenie i wyświetlenie wyznacznika
print(f"\nWyznacznik macierzy: {wyznacznik(macierz)}")
