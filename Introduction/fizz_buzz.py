# Fizz Buzz machine

print('What number shall we start from?')
start_val = int(input())
print(f"Cool! {start_val} is a good starting point. What number shall we end on?")
end_val = int(input())
print(f"Nice! We will finish at {end_val}")
print('What word should we say instead of multiples of 3?')
fizz = input().upper()
print('Lastly what should we say instead of multiples of 5?')
buzz = input().upper()

counter = start_val
while counter < end_val:
    counter += 1
    if counter % 15 == 0:
        print(f"{fizz} {buzz}!!!")
    elif counter % 3 == 0:
        print(fizz)
    elif counter % 5 == 0:
        print(buzz)
    else:
        print(counter)
