"""
CP1404/CP5632 - Practical
Program for password validation and star output
Mikhail Bovt
22/09/2025
"""
MIN_LENGTH = 6

def main():
    """Get and validate password, then print stars."""
    password = get_password()
    print_stars(password)


def get_password():
    """Prompt user for a valid password."""
    password = input("Enter password: ")
    while not is_valid_password(password):
        print(f"Invalid password. Must be at least {MIN_LENGTH} characters long and contain no spaces.")
        password = input("Enter password: ")
    return password


def is_valid_password(password):
    """Determine if password is considered valid."""
    return len(password) >= MIN_LENGTH and " " not in password


def print_stars(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))


main()
