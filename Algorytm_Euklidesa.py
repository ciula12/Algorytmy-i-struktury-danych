import math
import random

def nwd_iter(a, b):
    while b:
        a, b = b, a % b
    return a

def nwd_rek(a, b):
    if b == 0:
        return a
    return nwd_rek(b, a % b)

a = random.randint(1, 100)
b = random.randint(1, 100)

print(f"NWD iteracyjnie: {nwd_iter(a, b)}")
print(f"NWD rekurencyjnie: {nwd_rek(a, b)}")