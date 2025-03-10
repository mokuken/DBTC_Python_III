word = input("Enter a word:")
vowel_count = 0

for char in word:
    if char == 'a':
        print("a is a vowel")
        vowel_count+=1
    elif char == 'e':
        print("e is a vowel")
        vowel_count+=1
    elif char == 'i':
        print("i is a vowel")
        vowel_count+=1
    elif char == 'o':
        print("o is a vowel")
        vowel_count+=1
    elif char == 'u':
        print("u is a vowel")
        vowel_count+=1
    else:
        print(char)

print(f"\ntotal of vowels: {vowel_count}")