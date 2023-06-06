#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
description = ""
if number > 5:
    description = "and is greater than 5"
elif number == 0:
    description = "and is 0"
elif number > 6 and number != 0:
    description = "and is less than 6 and not 0"
print(f"last digit of {number} is {last_digit} {description}")
