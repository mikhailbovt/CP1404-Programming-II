"""
CP1404/CP5632 - Practical 3
Mikhail Bovt
05/10/2025
Exceptions To Complete
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit loop once valid input is received
    except ValueError:  # Catch only invalid number inputs
        print("Please enter a valid integer.")
print("Valid result is:", result)