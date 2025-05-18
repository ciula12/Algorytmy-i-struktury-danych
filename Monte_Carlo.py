import random
import math

def monte_carlo_pi(num_points: int) -> float:
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        distance = math.hypot(x, y) 
        if distance <= 1:
            inside_circle += 1

    return 4 * inside_circle / num_points

if __name__ == "__main__":
    points = 100_000
    pi_estimate = monte_carlo_pi(points)
    print(f"Oszacowana wartość π dla {points} punktów: {pi_estimate}")
    pi_estimate = monte_carlo_pi(points)
    print(f"Oszacowana wartość π dla {points} punktów: {pi_estimate}")
    pi_estimate = monte_carlo_pi(points)
    print(f"Oszacowana wartość π dla {points} punktów: {pi_estimate}")
    pi_estimate = monte_carlo_pi(points)
    print(f"Oszacowana wartość π dla {points} punktów: {pi_estimate}")
    pi_estimate = monte_carlo_pi(points)
    print(f"Oszacowana wartość π dla {points} punktów: {pi_estimate}")
