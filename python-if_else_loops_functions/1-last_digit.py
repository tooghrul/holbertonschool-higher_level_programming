#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(str(number)[-1])
text = f"Last digit of {number} is {last} and"
if last > 5:
    print(text, "is greater than 5")
elif last == 0:
    print(text, "is 0")
else:
    print(text, "is less than 6 and not 0")
