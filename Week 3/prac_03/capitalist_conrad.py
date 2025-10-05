"""
CP1404/CP5632 - Practical 3
Mikhail Bovt
05/10/2025
Capitalist Conrad
"""
import random

# Constants 
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "OUTPUT_CAPITALIST_CONRAD.txt"

# Setup 
price = INITIAL_PRICE
number_of_days = 0

out_file = open(FILENAME, 'w')

print(f"Starting price: ${price:,.2f}")
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulation Loop
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1

    # Decide whether price goes up or down
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Apply the change
    price *= (1 + price_change)

    print(f"On day {number_of_days} price is: ${price:,.2f}")
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()