#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digts = number - 10 * int(number / 10)
if digts > 5:
    print(f'Last digit of {number} is {digts} and is greater than 5')
elif digts < 6 and digts != 0:
    print(f'Last digit of {number} is {digts} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {digts} and is 0')
