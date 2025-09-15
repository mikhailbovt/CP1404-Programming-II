import random

print("Welcome to the secret number game!")
SECRET_NUMBER = random.randint(1, 10)
guess = int(input("Enter your guess: "))
while guess != SECRET_NUMBER:
    guess = int(input("Enter your guess: "))
print("Congratulations!")