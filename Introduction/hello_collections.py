# # Lists (aka arrays)
#
# shopping_list = ["apple", "banana", "cherry", 5]
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[0])
#
# shopping_list.append("mushrooms")
# print(shopping_list)
#
# shopping_list.remove(5)
# print(shopping_list)
#
# pop_return = shopping_list.pop()
# print(shopping_list)
# print(pop_return)
#
# print(shopping_list.pop(0))
# print(shopping_list)

# shopping_list[1] = "Berry"
# print(shopping_list)

# # Lists are MUTABLE


# # Tuples
#
# colours = ("blue", "purple", "turquoise")
# print(colours)
# print(type(colours))
# print(colours[-1])
#
# # Tuples are IMMUTABLE


# Dictionaries

my_dict = {"key": "value", "key2": 2}
# Key must be unique but value can be any data type

big_dict = {
    "key1": "value1",
    "key2": 2,
    "key3": [1,2,3]
}
print(big_dict)

kt_dict = {
    'First Name': "Katie",
    'Last Name': "McDonnell",
    'Age': 23,
    'D.O.B': "03/01/97",
    'siblings': ["Jim", "Lizzie", "Paddy"]
}
print(kt_dict)
print(kt_dict['Age'])

kt_dict['Key'] = 'new value'
print(kt_dict)

print(kt_dict.keys())
print(kt_dict.values())

data14 = {
    "trainees": ["Alex", "Joe", "Evie", "Jade"],
    "course": "Data Engineering",
    "start date": "15/06/2020"
}

print(data14["trainees"][0])
