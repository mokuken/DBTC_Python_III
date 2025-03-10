name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
birthYear = input("Enter your birth year: ")

birthYear_new = int(birthYear)

next_year_height = height + 5

print("\nUser Details")
print("Full Name", name)
print("Age", age)
print("Height", height)
print("Birth Year", birthYear)
print("Estimated Height Next Year", height + 0.05)
