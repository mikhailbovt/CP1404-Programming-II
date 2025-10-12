"""
CP1404/CP5632 - Practical 4
Mikhail Bovt
12/10/2025
Quick Pick" Lottery Ticket Generator
"""
import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    """Ask user how many quick picks to generate and print them."""
    quick_picks_count = int(input("How many quick picks? "))

    for _ in range(quick_picks_count):
        quick_pick = generate_quick_pick()
        # Format numbers in ascending order, 2 spaces wide each
        print(" ".join(f"{num:2}" for num in quick_pick))

def generate_quick_pick():
    """Generate one quick pick with unique random numbers."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


main()