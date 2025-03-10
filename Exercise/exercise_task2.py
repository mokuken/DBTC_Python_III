math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Charlie", "David", "Eve", "Frank"}

all_students = math_students.union(science_students)
print(all_students)

same_student = math_students.intersection(science_students)
print(same_student)

not_math_student = math_students.difference(science_students)
print(not_math_student)

not_student = math_students.symmetric_difference(science_students)
print(not_student)