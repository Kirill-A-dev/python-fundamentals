students = [
    {"name": "Alex", "grade": 4},
    {"name": "Maria", "grade": 5},
    {"name": "John", "grade": 3},
    {"name": "Bob", "grade": 2},
    {"name": "Anna", "grade": 5}
]

exc_students = []
good_students = []
bad_students = []
for student in students:
    if student["grade"] == 5:
        exc_students.append(student["name"])
    elif student["grade"] >= 4:
        good_students.append(student["name"])
    else:
        bad_students.append(student["name"])
print("Excellent students:")
for student in exc_students:
    print(student)
print("\nGood students:")
for student in good_students:
    print(student)
print("\nNeed improvement:")
for student in bad_students:
    print(student)
print("\nSummary:")
print("Excellent: ", len(exc_students))
print("Good: ", len(good_students))
print("Need improvement: ", len(bad_students))
print("\nTotal students: ", len(students))