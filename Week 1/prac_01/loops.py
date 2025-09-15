"""
CP1404 - Practical
Loops
Mikhail Bovt
15/09/2025
"""
# example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
print("a. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. 
print("b. Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
print("c. Print n stars:")
n = int(input("Number of stars: "))
for i in range(n):
    print("*", end='')
print()

# d. 
print("d. Print n lines of increasing stars:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end='')
    print()