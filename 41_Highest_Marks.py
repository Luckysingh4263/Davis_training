students = {"A": 80, "B": 95, "C": 78}

max_student = max(students, key=students.get)

print(max_student)