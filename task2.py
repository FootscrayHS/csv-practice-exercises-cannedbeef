# Task 2 — Filter by City
# Read students.csv and display only students from a given city.

students = []
file = open('students.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    students.append(fields)
file.close()

city_to_find = input('Enter a city: ')

# Your code below — find all students from that city

ST_NAME: int = 0
ST_AGE: int = 1
ST_CITY: int = 2

filtered_students = list(filter(
	lambda student: student[ST_CITY].casefold() == city_to_find.casefold(),
	students
))

if len(filtered_students) == 0:
	print(f"No students live in \"{city_to_find}\"")

else:
	print(f"All students who live in \"{city_to_find}\":")

	for student in filtered_students:
		print(f"\t{student[ST_NAME]}: {student[ST_AGE]}")
