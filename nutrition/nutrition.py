calories_list = [130,50,110,60,90,15,20,80,100,70]
answer =input('Item: ')
fruit_item = answer.lower()
if fruit_item == 'apple':
    print(calories_list[0])
elif fruit_item == 'avocado' or fruit_item == 'cantaloupe' or fruit_item == 'honeydew melon' or fruit_item == 'pineapple' or fruit_item == 'strawberries':
    print(calories_list[1])
elif fruit_item == 'banana':
    print(calories_list[2])
elif fruit_item == 'grapefruit' or fruit_item == 'nectarine' or fruit_item == 'peach':
    print(calories_list[3])
elif fruit_item == 'grapes' or fruit_item == 'kiwifruit':
    print(calories_list[4])
elif fruit_item == 'lemon':
    print(calories_list[5])
elif fruit_item == 'lime':
    print(calories_list[6])
elif fruit_item == 'orange' or fruit_item == 'watermelon':
    print(calories_list[7])
elif fruit_item == 'pear' or fruit_item == 'sweet cherries':
    print(calories_list[8])
elif fruit_item == 'plums':
    print(calories_list[9])