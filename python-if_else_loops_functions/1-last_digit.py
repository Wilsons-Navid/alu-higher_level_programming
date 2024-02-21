#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
is_negative = 0
if number < 0:
    number = abs(number)
    is_negative = 1
lastd = number % 10
if is_negative == 1:
    number = -abs(number)
    lastd = -abs(lastd)
print(f"Last digit of {number} is ", end="")
if lastd > 5:
    print(f"{lastd} and is greater than 5")
elif lastd == 0:
    print(f"{lastd} and is 0")
else:
    print(f"{lastd} and is less than 6 and not 0")
