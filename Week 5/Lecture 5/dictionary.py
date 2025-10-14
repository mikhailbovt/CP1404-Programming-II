from operator import itemgetter

name_and_age = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
# print(name_and_age)
# for name in sorted(name_and_age, key=lambda n: name_and_age[n], reverse=True):
#     print(name, "=", name_and_age[name])

name_width = max((len(name) for name in name_and_age.keys()))
print (name_width)

age_width = max((len(str(age)) for age in name_and_age.values()))
print(age_width)

for name, age in sorted(name_and_age.items(), key=itemgetter(1), reverse=True):
    print(f"{name:{name_width}} = {age:{age_width}}")