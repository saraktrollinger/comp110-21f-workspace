"""List utility functions part 2."""

__author__ = "730393060"


def only_evens(list_one: list[int]) -> list[int]:
    """Return a list of only the even numbers."""
    i: int = 0
    list_two: list[int] = list()
    while i <= len(list_one) - 1:
        if list_one[i] % 2 == 0:
            list_two.append(i)
        i += 1
    return list_two


def sub(initial: list[int], start: int, end: int) -> list[int]:
    """Return the initial list of start index until end index minus one."""
    i: int = 0 + start
    new_end: int = end - 1
    new_list: list[int] = list()
    while i <= new_end - 1:
        if i == len(initial):
            return new_list
        else:
            if start < 0:
                i = initial[0]
                new_list.append(i)
            else:
                new_list.append(i)
        i += 1
    return new_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Returns a list of both inputed lists."""
    new_str: list[int] = list()
    i: int = 0
    while i <= len(list_one) - 1:
        new_str.append(i)
        i += 1
    i: int = 0
    while i <= len(list_two) - 1:
        new_str.append(i)
        i += 1
    return new_str