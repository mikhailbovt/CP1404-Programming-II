print("Welcome to the secret number game!")
SECRET_NUMBER = 7
guess = int(input("Enter your guess: "))
while guess != SECRET_NUMBER:
    guess = int(input("Enter your guess: "))
print("Congratulations!")