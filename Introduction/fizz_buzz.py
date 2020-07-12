# Fizz Buzz machine



counter = 0

while counter <= 100:
    counter += 1
    if counter % 15 == 0:
        print('FIZZBUZZ')
    elif counter % 3 == 0:
        print('FIZZ')
    elif counter % 5 == 0:
        print('BUZZ')
    else:
        print(counter)
