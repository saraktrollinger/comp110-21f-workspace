"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730393060"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortuneone: int = 1
fortunetwo: int = 2
fortunethree: int = 3
fortunefour: int = 4

print("Your fortune cookie says...")

if randint(1, 4) == fortuneone:
    print("You will find love in a place you never expected.")
else:
    if randint(1, 4) == fortunetwo:
        print("There is a great struggle for you ahead.")
    else:
        if randint(1, 4) == fortunethree:
            print("You will meet a soulmate soon.")
        else:
            print("A friend is right around the corner.")

print("Now, go spread positive vibes!")