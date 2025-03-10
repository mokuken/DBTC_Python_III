# python_activity5.1

# Get user input for test score and bonus points
test_score = float(input("Enter your test score (0-100): "))
bonus_points = float(input("Enter your bonus points (0-10): "))

# Calculate final score and round to nearest whole number
final_score = round(test_score + bonus_points)

# Determine the grade
if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "B"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the final grade
print(f"Final Score: {final_score}, Grade: {grade}")
