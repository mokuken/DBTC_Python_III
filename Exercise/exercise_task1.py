student_grades = { 
    "harly":70,
    "ryan":80,
    "jemart":90
}

# add new student
student_grades["art"] = 85

# update student grade
student_grades["harly"] = 100

# delete student three
del student_grades["jemart"]


for student, grades in student_grades.items():
    print(f"Student name: {student} with grades of: {grades}")



