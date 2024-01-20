# Geting user input
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

# Conditons if true print yes
if answer.strip() == "42":
    print("Yes")
elif answer.lower() == "forty-two":
    print("Yes")
elif answer.lower() == "forty two":
    print("Yes")
# if false print no
else:
    print("NO")