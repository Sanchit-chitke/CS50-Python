# getting user input

camelCase = input("camelCase: ")
# print snake case

print("snake_case: ", end = "")
# looping through the input

for letter in camelCase:

    # applying the condition for finding the capital letter

    if letter.isupper():
        
        print("_" + letter.lower(),end="")
    else:
        print(letter, end= "")
print()