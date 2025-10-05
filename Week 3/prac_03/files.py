"""
CP1404/CP5632 - Practical 3
Mikhail Bovt
05/10/2025
Files
"""
# 1. Ask for user's name and write it to a file using open/close
name = input("Enter your name: ")
out_file = open("name.txt", "w") 
print(name, file=out_file)          
out_file.close()                    

# 2. Read the name from the file and greet the user
in_file = open("name.txt", "r")     
name_from_file = in_file.read().strip()  
in_file.close()
print(f"Hi {name_from_file}!")

# 3. Read the first two numbers from numbers.txt and print their sum

with open("numbers.txt", "r") as numbers_file:
    number1 = int(numbers_file.readline())
    number2 = int(numbers_file.readline())
    result = number1 + number2
print(result) 

# 4. Read all numbers from numbers.txt and print the total
with open("numbers.txt", "r") as numbers_file:
    total = 0
    for line in numbers_file:
        total += int(line)
print(total)