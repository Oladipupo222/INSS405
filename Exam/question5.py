def collect_final_grades(num_users):
    grades = []
    for _ in range(num_users):
        grade = float(input("Enter final grade: "))
        grades.append(grade)
    return grades

def calculate_mean(grades):
    mean = sum(grades) / len(grades)
    return mean

def assign_letter_grade(mean):
    if mean >= 90:
        letter_grade = 'A'
    elif mean >= 80:
        letter_grade = 'B'
    elif mean >= 70:
        letter_grade = 'C'
    elif mean >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return letter_grade

num_users = 3
final_grades = collect_final_grades(num_users)

mean_grade = calculate_mean(final_grades)

letter_grade = assign_letter_grade(mean_grade)

print("Final Grades:", final_grades)
print("Mean Grade:", mean_grade)
print("Letter Grade:", letter_grade)