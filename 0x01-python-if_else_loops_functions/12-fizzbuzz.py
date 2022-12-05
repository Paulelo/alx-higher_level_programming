#!/usr/bin/python3
for i in range(1, 101):
    fizz = 'Fizz'
    buzz = 'Buzz'
    fizzbuzz= 'FizzBuzz'

    if ((i % 3) == 0) and ((i % 5) == 0):
        print('{}'.format(buzz), end=" ")
    elif ((i % 3) == 0):
        print('{}'.format(fizz), end=" ")
    elif ((i % 5) == 0):
        print('{}'.format(buzz), end=" ")
    elif ((i % 3) == 0) and ((i % 5) == 0):
        print("{}".format(fizzbizz), end=" ")
    else:
        print("{}".format(i), end=" ")
