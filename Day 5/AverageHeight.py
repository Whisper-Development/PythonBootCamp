student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0

for heights in student_heights:
    total += heights

number_of_students = 0

for students in student_heights:
    number_of_students += 1

average_h = round(total/number_of_students)

print(average_h)