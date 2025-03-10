exam_scores = (85, 90, 78, 92, 88)

print(f"\nthe highest score is: {max(exam_scores)} and the lowest score is: {min(exam_scores)}\n")
print(f"The 78 number shows only {exam_scores.count(78)} time")

converted_tuple = list(exam_scores)

converted_tuple.append(100)

new_exam_scores = tuple(converted_tuple)

sliced_tuple =  new_exam_scores[0:3]

print(f"exam scores in tuple \n {exam_scores}\n")
print(f"converted back to tuple with new score \n {new_exam_scores}\n")
print(f"The sliced tuple and show the first three score \n {sliced_tuple}\n")
