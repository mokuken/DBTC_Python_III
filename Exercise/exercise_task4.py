exam_scores = (85, 90, 78, 92, 88)

print(f"\nthe highest score is: {max(exam_scores)} and the lowest score is: {min(exam_scores)}\n")
print(f"The 78 number shows only {exam_scores.count(78)} time")

# convert the tuple to list
converted_tuple = list(exam_scores)

# add 100 to the list
converted_tuple.append(100)

# convert the list back to tuple
new_exam_scores = tuple(converted_tuple)

# slice the tuple to show the first three score
sliced_tuple =  new_exam_scores[0:3]

print(f"exam scores in tuple \n {exam_scores}\n")
print(f"converted back to tuple with new score \n {new_exam_scores}\n")
print(f"The sliced tuple and show the first three score \n {sliced_tuple}\n")
