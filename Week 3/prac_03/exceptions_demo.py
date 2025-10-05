"""
CP1404/CP5632 - Practical 3
Mikhail Bovt
05/10/2025
Exceptions Demo
Answer the following questions:
1. When will a ValueError occur?
- When the user enters something that cannot be converted to an integer.

2. When will a ZeroDivisionError occur?
- When the user enters 0 as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes, by adding a check to ensure the denominator is not 0.

"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Prevent ZeroDivisionError
    while denominator == 0:
        print("Cannot divide by zero! Please enter a non-zero denominator.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")