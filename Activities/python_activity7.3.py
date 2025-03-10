num = input(f"Enter number: ")

numbers = [
    int(number) for number in num.split()
]

largest_numb = numbers[0] 
for number in numbers:
    if number > largest_numb:
        largest_numb = number

print(f"The largest number is: {largest_numb}")
