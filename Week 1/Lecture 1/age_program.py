age = int(input("Enter your age: "))
if age <= 4:
    category = "baby"       
elif age <= 17:
    category = "child"
elif age <= 65:
    category = "adult"
else:
    category = "old"
print(f"Your age {age} is considered that you are {category}")
