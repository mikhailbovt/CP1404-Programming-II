import random
def main():
    high_number, low_number = get_number()
    smiley_face(high_number, low_number)
    
def get_number():
    high_number = int(input("Enter the high number: "))
    while high_number <= 0:
        print("Higher number must be greater than 0")
        high_number = int(input("Enter the high number: "))
    low_number = int(input("Enter the low number: "))
    while high_number <= low_number:
        print("Lower number must be less than the higher number")
        low_number = int(input("Enter the low number: "))
    return high_number, low_number

def smiley_face(high_number, low_number):
    smiles_number = random.randint(low_number, high_number)
    print(":)" * smiles_number)


main()