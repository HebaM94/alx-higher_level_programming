#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = "Last digit of"
if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = number % -10
if lastDigit > 5:
    print(f"{i} {number} is {lastDigit} and is greater than 5")
elif lastDigit == 0:
    print(f"{i} {number} is {lastDigit} and is 0")
else:
    print(f"{i} {number} is {lastDigit} and is less than 6 and not 0")
