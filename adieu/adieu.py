import inflect

p = inflect.engine()
# Crating a list to store the names
names = []
# Looping forever
while True:
    try:
        # Get the user input
        name = input("Name: ")
        # Storing the names in the list we created
        names.append(name)
    except EOFError:
        # Create new line
        print()
        break
# Printing using inflect module
output = p.join(names)
print("Adieu, adieu, to",output)