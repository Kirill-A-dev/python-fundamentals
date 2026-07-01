students = [
    {"name": "Alex", "grades": [5, 4, 5]},
    {"name": "Maria", "grades": [5, 5, 5]},
    {"name": "John", "grades": [3, 4, 3]},
]

with open("students_report.txt", "w") as file:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = sum(grades)/len(grades)
        if average >= 4.5:
            status = "excellent"
        elif average >= 3.5:
            status = "good"
        else:
            status = "needs improvement"            
        file.write(f'{name}: average grade = {average:.2f}, status = {status}\n')

print("student report created succesfully.")