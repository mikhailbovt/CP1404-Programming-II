"""
CP1404/CP5632 - Practical 3
Mikhail Bovt
05/10/2025
Password Checker
"""
MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters:", SPECIAL_CHARACTERS)

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")

def is_valid_password(password: str) -> bool:
    """Determine if the provided password is valid based on the set rules."""
    # 1) Check the password length
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    # 2) Count the character types
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for character in password:
        if character.islower():
            count_lower += 1
        elif character.isupper():
            count_upper += 1
        elif character.isdigit():
            count_digit += 1
        elif character in SPECIAL_CHARACTERS:
            count_special += 1

    # 3) Check that the password meets the required criteria
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if IS_SPECIAL_CHARACTER_REQUIRED and count_special == 0:
        return False

    # If all conditions are met, the password is valid
    return True

main()