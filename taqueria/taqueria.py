# create a dictionary of menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# set the total amount to zero
total_amount = 0
#loop forever
while True:
    try:
        # Get user input
        item = input("Item: ").title()
        # check if the item is in the menu dictonary
        if item in menu:
            # add item amount in total amount
            total_amount += menu[item]
            # Print the current total
            print("Total: $",end="")
            print("{:.2f}".format(total_amount))
    except EOFError:
        print()
        break