# Fizz Buzz machine

def not_int(prompt):
    val = ""
    while not val.isnumeric():
        val = input(prompt)
        if not val.isnumeric():
            print('Thats not a number lets try again')
    return int(val)


start = not_int('What is your start number?')

end = not_int('What is your end number?')

print('What word should we say instead of multiples of 3?')
fizz = input().upper()
print('Lastly what should we say instead of multiples of 5?')
buzz = input().upper()

counter = start
while counter < end:
    counter += 1
    if counter % 15 == 0:
        print(f"{fizz} {buzz}!!!")
    elif counter % 3 == 0:
        print(fizz)
    elif counter % 5 == 0:
        print(buzz)
    else:
        print(counter)

