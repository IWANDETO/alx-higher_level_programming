#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if str(number)[-1] > '5':
	print(f"Last digit of {number} is {str(number)[-1]} and is greater than 5\n")
elif str(number)[-1] == '0':
        print(f"Last digit of {number} is {str(number)[-1]} and is 0\n")
else:
        print(f"Last digit of {number} is {str(number)[-1]} and is less than 6 and not 0\n")
