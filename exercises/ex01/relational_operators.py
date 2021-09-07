"""True or false: bool edition."""
__author__ = "730393060"

side1: str = input("Left-hand side: ")
side2: str = input("Right-hand side: ")
first_op = int(side1) < int(side2)
second_op = int(side1) >= int(side2)
third_op = int(side1) == int(side2)
fourth_op = int(side1) != int(side2)
print(side1 + " < " + side2 + " is " + str(first_op))
print(side1 + " >= " + side2 + " is " + str(second_op))
print(side1 + " == " + side2 + " is " + str(third_op))
print(side1 + " != " + side2 + " is " + str(fourth_op))