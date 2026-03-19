# Task 1 — Display All Students
# Read students.csv and display each student's details.

students = []
file = open('students.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    students.append(fields)
file.close()

# Your code below — use the students list

ST_NAME: int = 0
ST_AGE: int = 1
ST_CITY: int = 2

for student in students:
	print(f"{student[ST_NAME]} is {student[ST_AGE]}, and lives in {student[ST_CITY]}")
