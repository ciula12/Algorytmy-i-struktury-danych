import random
import math

# Funkcja celu
def fitness(x: float) -> float:
    return x * math.sin(x)

# Tworzy losowego osobnika
def create_individual() -> float:
    return random.uniform(0, 10)

# Mutacja: lekkie przesunięcie wartości x
def mutate(x: float, mutation_rate=0.1) -> float:
    mutation = random.uniform(-mutation_rate, mutation_rate)
    x_new = x + mutation
    return min(max(x_new, 0), 10)  # zapewnia zakres [0, 10]

# Selekcja turniejowa
def select(population, k=3):
    selected = random.sample(population, k)
    return max(selected, key=fitness)

# Główna funkcja algorytmu ewolucyjnego
def evolutionary_algorithm(pop_size=100, generations=50, mutation_rate=0.1):
    population = [create_individual() for _ in range(pop_size)]

    for generation in range(generations):
        new_population = []
        for _ in range(pop_size):
            parent = select(population)
            child = mutate(parent, mutation_rate)
            new_population.append(child)
        population = new_population

        best = max(population, key=fitness)
        print(f"Pokolenie {generation+1}: najlepszy x = {best:.4f}, f(x) = {fitness(best):.4f}")

    return max(population, key=fitness)

# Przykład użycia
if __name__ == "__main__":
    best_solution = evolutionary_algorithm()
    print(f"\nNajlepsze rozwiązanie: x = {best_solution:.4f}, f(x) = {fitness(best_solution):.4f}")
