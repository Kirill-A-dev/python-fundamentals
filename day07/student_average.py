students = [
    {"name": "Alex", "grades": [5, 4, 5]},
    {"name": "Maria", "grades": [4, 4, 3]},
    {"name": "John", "grades": [2, 3, 2]},
]

for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    if average >= 4.5:
        status = "excellent"
    elif average >= 3.5:
        status = "good"
    else:
        status= "needs improvement"
    print(f'Name: {name}')
    print(f'Grades: {grades}')
    print(f'Average: {round(average, 2)}')
    print(f'Status: {status}')
    print(30 * "_")