#
# hw = "Hello World!"
#
# print(len(hw))
#
# #  0 1 2 3 4 5 6 7 8 9 10 11
# #  H e l l o   W o r l d  !
#
# print(hw[6])
# print(hw[3:7])
# print(hw[4:])
# print(hw[:8])
#
# print(hw[-11])
# print(hw[-10:-5])
# print(hw[-7:])
#
# white_space = "       white space       "
#
# print(len(white_space))
# print(white_space.strip())
# print(white_space.lstrip())
# print(white_space.rstrip())
# print(white_space.count(" "))
# print(white_space.lower())
# print(white_space.upper())
# print(white_space.strip().capitalize())
# print(white_space.replace("space", "noise"))
# print(white_space.strip())
#
# a = "Aardvark"
# b = "Bat"
# c = "Cheshire Cat"
# d = 5
#
# print(a + ", " + b + ", " + c + ", " + str(d))
#
# num = "54"
# print(type(int(num)))
#
# print(f"{a}, {b}, {c}, {d}")
#
# name = "Katie"
# print(f"Hello my name is {name}!")

print("Hi, What is your name?")
name = input()
print(f"Hi {name}! How old are you?")
age = input()
print(f"Wow you are {age}! How many siblings do you have?")
siblings = input()
print(f"Cool, {siblings} siblings is fun! What is your favourite decimal number {name}?")
dec_num = input()
print(f"{dec_num} is my favourite too! What is your favourite animal?")
animal = input()
print(f"{animal}'s are cool animals!")
