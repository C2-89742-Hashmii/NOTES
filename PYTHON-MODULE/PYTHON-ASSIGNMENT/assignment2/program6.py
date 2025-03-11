# The marks obtained by a student in 3 different subjects are input by the user. Your program should
# calc ulate the average of subjects and display the grade. The student gets a grade as per the following
# rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

average = (marks1 + marks2 + marks3) / 3
if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average <= 89:
    grade = 'B'
elif 70 <= average <= 79:
    grade = 'C'
elif 60 <= average <= 69:
    grade = 'D'
else:
    grade = 'F'


print(f"Average marks: {average:.2f}")
print(f"Grade: {grade}")