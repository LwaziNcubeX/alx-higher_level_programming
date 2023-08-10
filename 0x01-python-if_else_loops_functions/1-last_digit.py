#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
text = " and is less than 6 and not 0"

if lastDigit > 5 and number > 0:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
elif 0 < lastDigit < 6 and number > 0:
    print(f"Last digit of {number} is {lastDigit}{text}")
else:
    print(f"Last digit of {number} is -{lastDigit}{text}")
