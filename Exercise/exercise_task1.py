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


for name, grades in student_grades.items():
    print(f"Student name: {name} with grades of: {grades}")



