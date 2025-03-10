word = input("Enter a word:")

for char in reversed(word):
    print((char))

print(f"\n{word[::-1]}")