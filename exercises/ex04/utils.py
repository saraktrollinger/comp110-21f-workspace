"""List utility functions."""

__author__ = "730393060"


# TODO: Implement your functions here.


def all(user: int, xs: list[int]) -> bool:
    """Return True if all ints in list are same, False otherwise."""
    i: int = 0
    while i < len(xs):
        if user != xs[i]:
            return False
        i += 1
    return True


def is_equal(one: list[int], two: list[int]) -> bool:
    """Return True if both lists are the same at each index, False otherwise."""
    i: int = 0
    while i < len(one) or len(two):
        if one[i] != two[i]:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Return the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest: int = input[0]
    while i < len(input):
        if input[i] > largest:
            largest = input[i]
            i += 1
    print(largest)
    return largest