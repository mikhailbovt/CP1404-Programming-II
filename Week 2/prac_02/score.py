"""
CP1404/CP5632 - Practical
Program to determine score status
Mikhail Bovt
22/09/2025
"""

"""Program to determine score status using functions"""

import random


def main():
    """Get user score, classify it, then generate and classify a random score."""
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(f"Your result: {result}")

    random_score = random.uniform(0, 100)
    random_result = determine_score_result(random_score)
    print(f"Random score: {random_score:.2f} → {random_result}")


def determine_score_result(score):
    """Return the classification of a score as a string."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
