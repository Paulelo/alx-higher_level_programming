#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f'The number is {number}')
if number >= 10:
	number = number % 10
	print(f'The number is {number}')

	if number > 5:
		print(f'Last digit of {number + 10} is {number} and is greater than 5')
	elif number == 0:
		print(f'Last digit of {number + 10} is {number} and is 0')
	elif number < 6:
		print(f'Last digit of {number + 10} is {number} and is greater than 0')
	print(f'The number is {number}')
