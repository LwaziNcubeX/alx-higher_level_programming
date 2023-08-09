#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number
if lastDigit > 5:
    print(f"Last digit of {number} is "+ str(lastDigit)[-1:] +" and is greater than 5")
elif lastDigit == 0:
    print(f"Last digit of {number} is "+ str(lastDigit)[-1:] +" and is 0")
elif lastDigit < 6 & lastDigit > 0:
    print(f"Last digit of {number} is "+ str(lastDigit)[-1:] +" and is less than 6 and not 0")
else:
    print(number)
