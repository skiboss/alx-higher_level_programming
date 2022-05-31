#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
no = str(number)
last_digit = int(no[-1])
result = f"Last digit of {number} is {last_digit}"

if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    print(f"{result} and is greater than 5")
elif last_digit == 0:
    print(f"{result} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"{result} and is less than 6 and not 0")
