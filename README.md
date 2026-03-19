[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23204850)
# Reading CSV Files in Python
### VCE Applied Computing — Unit 1, Area of Study 2

---

## Before you start

**Read the learning activity on Google Classroom first.**

The activity walks you through the reading pattern, explains what happens in memory after loading a file, and gives you annotated examples to refer back to. You will not get far with these tasks without reading it first.

> 📋 **Find it on Google Classroom:** Unit 1 AOS 2 → Reading CSV Files in Python

---

## Files in this repo

| File | What it is |
|---|---|
| `students.csv` | Student name, age, and city — used in Tasks 1 and 2 |
| `scores.csv` | Student name and quiz score — used in Task 3 and the Extension |
| `task1.py` | Starter file for Task 1 |
| `task2.py` | Starter file for Task 2 |
| `task3.py` | Starter file for Task 3 |
| `taskE.py` | Starter file for the Extension task |

---

## The tasks

### Task 1 — Display All Students
Read `students.csv` into memory and display each student's name, age, and city in a sentence.

The reading pattern is already written for you. Add your code below the comment that says `# Your code below`.

### Task 2 — Filter by City
Read `students.csv` into memory. The program will ask the user to enter a city, then display only the students who live there.

Again — the reading pattern is done. Your job is to loop through the list and filter by the city field.

### Task 3 — Read a Different File and Use a Provided Function
Read `scores.csv` into memory and display each student's name, score, and grade.

A `get_grade()` function has been provided at the top of `task3.py` — do not change it. Call it with the score field from each record to get the grade string.

### Extension — Write Back to the File
Read `scores.csv`, add a new student entered by the user, then write the entire updated list back to the file so the new record is saved.

Only attempt this after completing Tasks 1–3.

---

## How to work in your Codespace

1. Open your repository on GitHub
2. Open the relevant `.py` file in the editor
3. Write your code below the `# Your code below` comment
4. Test/Run your files. You can also start them using the terminal, eg.: `python task1.py`

---

## A reminder about the reading pattern

Every starter file uses the same seven lines to load the CSV. You will see this pattern a lot:

```python
data = []
file = open('filename.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    data.append(fields)
file.close()
```

After these lines run, `data` is a list of lists. Each inner list is one row from the file. Access values with two indexes — `data[row][column]` — both starting from 0.
