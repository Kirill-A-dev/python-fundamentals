student = {
    "name": "Alex",
    "age": 20,
    "grade": 5
}
print(student)
print(student["name"])
print(student["age"])
print(student["grade"])

student["grade"] = 4
print(student)
print(student["grade"])

print(type(student["age"]))
print(type(student["grade"]))
print(type(student["name"]))

student["city"] = "Berlin"
print(student)
print(student["city"])

del(student["city"])
print(student)

if 'city' in student:
    print(student["city"])
else:
    print("City not found")

print(student.get("name"))
print(student.get("age"))
print(student.get("city"))
print(student.get("city", "City not found"))

for key in student:
    print(key)

for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)

print(student.keys())
print(student.values())

for key in student.keys():
    print("Key:", key)
for value in student.values():
    print("Value:", value)
