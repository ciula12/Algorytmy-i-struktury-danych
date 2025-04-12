import random
import matplotlib.pyplot as plt
import numpy as np

def bisekcja_z_losowoscia(f, a, b, tol=1e-6, max_iter=100):
    # Losowanie początkowych punktów a i b w przedziale [a, b]
    while True:
        a_random = random.uniform(a, b)
        b_random = random.uniform(a, b)
        
        # Upewnijmy się, że f(a) * f(b) < 0
        if f(a_random) * f(b_random) < 0:
            a, b = a_random, b_random
            break  # Przerywamy, gdy warunek jest spełniony
    
    print(f"Losowy przedział: a = {a}, b = {b}")
    
    iter_count = 0
    
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2  # punkt środkowy
        if f(c) == 0:  # znaleziono dokładne miejsce zerowe
            return c
        elif f(a) * f(c) < 0:
            b = c  # zmniejszamy przedział do [a, c]
        else:
            a = c  # zmniejszamy przedział do [c, b]
        
        iter_count += 1
    
    return (a + b) / 2  # zwróć przybliżoną wartość miejsca zerowego

# Przykład użycia:
def f(x):
    return x**2 - 4  # Funkcja x^2 - 4

# Szukamy miejsca zerowego w przedziale [1, 3]
a = 1
b = 3
result = bisekcja_z_losowoscia(f, a, b)

if result is not None:
    print(f"Przybliżone miejsce zerowe: {result}")

# Wykres funkcji oraz przedziału
x = np.linspace(a - 1, b + 1, 400)  # zakres wykresu (z większym marginesem)
y = f(x)

plt.plot(x, y, label="f(x) = x^2 - 4", color='blue')  # wykres funkcji
plt.axhline(0, color='black',linewidth=1)  # oś X
plt.axvline(0, color='black',linewidth=1)  # oś Y

# Zaznaczamy początkowy losowy przedział na wykresie
plt.plot([a, b], [f(a), f(b)], color='red', marker='o', linestyle='-', label=f"Losowy przedział: [{a}, {b}]")

# Dodanie tytułu i legendy
plt.title("Wykres funkcji i losowy przedział szukania miejsca zerowego")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Wyświetlenie wykresu
plt.grid(True)
plt.show()
