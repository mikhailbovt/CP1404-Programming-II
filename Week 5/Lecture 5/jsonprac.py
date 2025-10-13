import json

json_name_and_age = '{"Bill": 21, "Jane": 30, "Sven": 56}'

# print(json_name_and_age)
# print(json_name_and_age["Jane"])

name_and_age = json.loads(json_name_and_age)
print(name_and_age)
print(name_and_age["Jane"])

