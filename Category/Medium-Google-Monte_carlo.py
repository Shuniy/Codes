"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal
places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

from random import random

radius = 2

def estimate_pi(num_random_tests):
    pi_counter = 0
    r_squared = radius ** 2
    for _ in range(num_random_tests):
        x_rand = random() * radius
        y_rand = random() * radius
        if (x_rand ** 2) + (y_rand ** 2) < r_squared:
            pi_counter += 1
    return 4 * pi_counter / num_random_tests

assert round(estimate_pi(100000000), 3) == 3.141
