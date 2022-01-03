#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    digit = number % 10
elif number < 0:
    digit = number % -10
else:
    digit = 0
if digit > 0:
    digit = number % 10
elif digit < 0:
    digit = number % -10
else:
    digit = 0
if digit > 5:
    bit = "greater than 5"
elif digit == 0:
    bit = "0"
else:
    bit = "less than 6 and not 0"
print("Last digit of {:d} is {:d} and is {}".format(number, digit, bit))
