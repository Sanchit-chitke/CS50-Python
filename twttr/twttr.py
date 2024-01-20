# get the input from user
sentence = input("Input: ")

print("Output: ", end="")
# loop through the input
for letter in sentence:
# find the vowels to ommit
    if not letter.lower() in ['a','e','i','o','u']:
        print(letter,end="")
print()