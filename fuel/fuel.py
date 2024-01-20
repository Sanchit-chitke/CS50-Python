#start of the while loop
while True:
    # get the user input
    fuel = input("Fraction: ")

    try:

        # Splitting the input into numerator and denomenator
        numerator, denomenator = fuel.split("/")
        # conversion of string to the int
        x = int(numerator)
        y = int (denomenator)

        # doing the division of the input
        f = x / y

        if f <= 1:
            break
    except (ValueError,ZeroDivisionError):
        pass
# converting the division to the percentage
p = int(round(f * 100))

# if the percentage is less than 1 print E
if p <= 1:
    print("E")
# if the percentage is grater or equal to 99 print F
elif p >= 99:
    print("F")
# otherwise print the percentage of the fuel
else:
    print(f"{p}%")