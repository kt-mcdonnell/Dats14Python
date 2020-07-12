# Fizz Buzz machine

print('What number shall we start from?')
start_val = int(input())
print(f"Cool! {start_val} is a good starting point. What number shall we end on?")
end_val = int(input())


counter = start_val

while counter < end_val:
    counter += 1
    if counter % 15 == 0:
        print('FIZZBUZZ')
    elif counter % 3 == 0:
        print('FIZZ')
    elif counter % 5 == 0:
        print('BUZZ')
    else:
        print(counter)
