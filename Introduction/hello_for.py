# For Loops

shopping_list = ["eggs", "bacon", "bread"]

for item in shopping_list:
    print(item)


shopping_list = ["eggs", "bacon", "bread"]
colours = ["yellow", "purple", "turquoise"]

for item in shopping_list:
    for colour in colours:
        print(colour, item)

dict_data = {
    1: {"name": "Alex", "animal": "all dogs"},
    2: {"name": "Ben", "animal": "flamingo"},
    3: {"name": "Evie", "animal": "gorilla"},
    4: {"name": "Charlotte", "animal": "giraffe"}
}

for key in dict_data:
    for inner_key in dict_data[key]:
        print(dict_data[key][inner_key])

for key in dict_data:
    print(f"{dict_data[key]['name']}'s favourite animal is {dict_data[key]['animal']}!")


# Chinese Menu

chinese_menu = {
    101: {'dish': 'egg fried rice', 'price': 1.90},
    102: {'dish': 'chicken fried rice', 'price': 4.90},
    103: {'dish': 'special fried rice', 'price': 5.10},
    115: {'dish': 'duck pancakes', 'price': 6.90},
    201: {'dish': 'sweet and sour chicken', 'price': 6.50},
    202: {'dish': 'crispy chilli beef', 'price': 6.80}
}

for item in chinese_menu:
    print(f"{chinese_menu[item]['dish']} costs £{chinese_menu[item]['price']:.2f} per portion.")