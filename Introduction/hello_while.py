# While Loops

counter = 0
while counter < 10:
    print(f"Still counting! {counter}")
    if counter == 6:
        break
    counter += 1

print('We escaped the while loop')

age = ""

while not age.isnumeric():
    age = input("Enter your age:\n")
    if age.isnumeric():
        age = int(age)
        break
    else:
        print("That's not a number, try again!")

print(f"You are {age}!")