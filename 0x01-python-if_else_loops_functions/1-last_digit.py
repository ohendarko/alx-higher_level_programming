#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lasdig = number % 10
if number < 0:
    lasdig = 10 - lasdig
    lasdig = -lasdig
if lasdig > 5:
    print(f"Last digit of {number} is {lasdig} and is greater than 5")
if lasdig == 0:
    print(f"Last digit of {number} is {lasdig} and is 0")
if lasdig < 6 and lasdig != 0:
    print(f"Last digit of {number} is {lasdig} and is less than 6 and not 0")
