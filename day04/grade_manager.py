students = []
grades = []
while True :
    name = input(" Enter students: ")
    if name == "stop" :
        break

    while True:
        grade_input = input(" Enter grade: ")
        if not grade_input.isdigit():
            print("Grade must be a number")            
            continue
        grade = int(grade_input)
        if grade < 1 or grade >5:
            print("Grade must be between 1 and 5")
            continue
        break        
    students.append(name)
    grades.append(grade)

print("\n--- Grade Report ---")

for i in range(len(students)) :
    print(f'{students[i]} - {grades[i]}')

if len(grades) > 0 :
    print(f'\nTotal students: {len(students)}')    
    average_grade = round((sum(grades))/len(grades), 2)
    highest_grade = max(grades)
    lowest_grade = min(grades)
    best_students = []
    for i in range(len(students)):
        if grades[i] == highest_grade:
            best_students.append(students[i])
    worst_students = []
    for i in range(len(students)):
        if grades[i] == lowest_grade:
            worst_students.append(students[i])
    best_students_text = ", ".join(best_students)
    worst_students_text = ", ".join(worst_students)
    print(f'\nAverage grade: {average_grade}')        
    print(f'Best students : {best_students_text} - {highest_grade}')
    print(f'Worst students : {worst_students_text} - {lowest_grade}')
else :
    print("\n--- No students added ---")




