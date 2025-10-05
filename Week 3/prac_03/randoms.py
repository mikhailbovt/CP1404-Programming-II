"""
CP1404/CP5632 - Practical 3
Mikhail Bovt
05/10/2025
Random Numbers
"""
import random

# Line 1
print(random.randint(5, 20))
# Smallest possible: 5
# Largest possible: 20

# Line 2
print(random.randrange(3, 10, 2))
# Smallest possible: 3
# Largest possible: 9
# Could it produce a 4? No, because the step is 2, so only odd numbers are possible.

# Line 3
print(random.uniform(2.5, 5.5))
# Smallest possible (approximately): 2.5
# Largest possible (approximately): 5.5

# Code to produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)