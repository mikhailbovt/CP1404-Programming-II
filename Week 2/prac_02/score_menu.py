"""
CP1404/CP5632 - Practical
Menu-based score program using functions
Mikhail Bovt
22/09/2025
"""

def main():
    """Run the score menu program."""
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid option")


def print_menu():
    """Print the main menu options."""
    print("\nMenu:\n(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit")


def get_valid_score():
    """Prompt user for a score between 0 and 100 inclusive."""
    score = float(input("Enter score (0–100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0–100): "))
    return score


def determine_score_result(score):
    """Return the classification of a score as a string."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print stars equal to the integer part of the score."""
    print("*" * int(score))


main()
