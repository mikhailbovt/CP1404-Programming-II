name = str(input("Enter your name: ")).upper()
while name == "":
    name = str(input("Enter your name: ")).upper()
print(f"Hello {name}!")
salary = float(input("Enter your salary: "))
while salary <= 0:
    salary = float(input("Enter your salary: "))
print(f"Your salary is ${salary:.2f}")