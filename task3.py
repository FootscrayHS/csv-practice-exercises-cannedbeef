# Task 3 — Read a Different File and Use a Provided Function
# Read scores.csv and display each student's name, score, and grade.

# This function has been provided for you — do not change it
def get_grade(score):
    score = int(score)
    if score >= 80:
        return 'Distinction'
    elif score >= 60:
        return 'Credit'
    elif score >= 40:
        return 'Pass'
    else:
        return 'Fail'


results = []
file = open('scores.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    results.append(fields)
file.close()

# Your code below — loop through results and display each student's grade
# Use get_grade(score) to get the grade string — e.g. get_grade(results[0][1])

for student in results:
	print(f"{student[0]} got {student[1]}% ({get_grade(int(student[1]))})")
