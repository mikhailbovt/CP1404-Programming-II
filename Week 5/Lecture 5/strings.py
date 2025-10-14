animals = ["cat", "dog", "capibara"]
for name in animals:
    print(name)

animals_to_length = {}
for name in animals:
    animals_to_length[name] = len(name)
print(animals_to_length)
