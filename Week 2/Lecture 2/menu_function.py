"""Menu Function with 4 options"""
import random

"""Main function"""
def main():
    print_menu()

"""Print menu function"""
def print_menu():
    MENU = """(N)ot empty name
(L)ine of asteriks
(R)andom number
(Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    menu_function(choice)

"""Menu function"""
def menu_function(choice):
    if choice == "N":
        not_empty_name()
    elif choice == "L":
        line_of_asteriks()
    elif choice == "R":
        random_number()
    elif choice == "Q":
        print("Farewell")
    else:
        print("Invalid choice")
        print_menu()

"""Not empty name function for validation"""
def not_empty_name():
    name = input("Enter your name: ")
    while name == "":
        print("Name cannot be empty")
        name = input("Enter your name: ")
    print(f"Hello {name}")
    print_menu()

"""Line of asteriks function"""
def line_of_asteriks():
    length = int(input("Enter the length of the line: "))
    print("*" * length)
    print_menu()

"""Random number function from 1 to 100"""
def random_number():
    number = random.randint(1, 100)
    print(f"Random number: {number}")
    print_menu()

main()