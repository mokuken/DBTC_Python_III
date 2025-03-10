number_rounds = int(input("\nEnter the number of rounds (1-10): "))
target_score = int(input("Enter the target score (0-100): "))

round_scores = []
total_score = 0
bonus_points = 0
deductions = 0

deduction_count = 0
for round_num in range(1, number_rounds + 1):
    score = int(input(f"Enter score for round {round_num} (0-100): "))
    round_scores.append(score)
    total_score += score

    if score >= target_score:
        bonus_points += 10
    elif round_num == 3:
        print(f"Warning! Low score in round {round_num}")

# Apply deductions if necessary
total_before_deductions = total_score + bonus_points
final_score = total_before_deductions

while final_score > 200:
    final_score -= 5
    deduction_count += 1

deductions = deduction_count * 5
average_score = total_score / number_rounds

# Display results
print("\nResults:")
print(f"Total before deductions: {total_before_deductions:.2f}")
print(f"Deductions applied: {deduction_count} (-{deductions})")
print(f"Final total: {final_score:.2f}")
print(f"Average score: {average_score:.2f}")

# Performance evaluation
if final_score > target_score:
    print("Great Job!")
elif final_score < target_score * 0.75:
    print("Try Harder!")
else:
    print("Solid Effort!")

# Bonus summary
if bonus_points == number_rounds * 10:
    print("Bonus Master!")
else:
    print(f"Total Bonus Earned: {bonus_points}\n")
