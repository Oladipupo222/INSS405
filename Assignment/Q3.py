scores = []
num_courses = 10
for i in range(num_courses):
    score = int(input("Enter the final score for course"))


total_score = sum(scores)
average_score = total_score / num_courses

if average_score > 90:
    grade = "A"
elif average_score > 80:
    grade = "B"
elif 75 <= average_score <= 79:
    grade = "C"
elif average_score > 60:
    grade = "D"
else:
    grade = "F"


print("Total score: ",(total_score))
print("Average score=",(average_score))
print("Grade:",(grade))