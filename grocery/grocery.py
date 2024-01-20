# creating a empty dict
grocery = {}

#looping forever
while True:
    try:
        # getting the user input
        item = input().lower()
        # checking if the item is already in the grocery
        if item in grocery:
            # if it is in grocery add 1 to count
            grocery[item] += 1
            # otherwise add the item for the first time
        else:
                grocery[item] = 1
    except EOFError:
        
        # print all the items in alphabetical order
        for key in sorted (grocery.keys()):
            print(grocery[key],key.upper())
            # stop the while loop

        break