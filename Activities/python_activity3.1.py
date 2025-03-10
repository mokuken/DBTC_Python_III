name = input("Enter your name: ")
weight = float(input("Enter your weight: "))
steps_walked = int(input("Steps walked: "))
years_exer = int(input("What year you started exercising: "))

next_month_weight = weight - 0.2
exercise_estimated = 2025 - years_exer

print("\nName: ", name)
print("Next Month Weight: ", next_month_weight)
print("Steps Walked: ", steps_walked)
print("You have been exercising for: ", exercise_estimated, "years")