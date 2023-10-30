# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exams scores.

# Write a program that convert their scores to grades and forms a new dictonary.

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# TODO1: Create an empty dictionary called student_grades

student_grades = {}

# TODO2: write the code below to add the grades to student_grades

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)