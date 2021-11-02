"""Practice with dictionaries."""

__author__ = "730393060"


def invert(initial: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    new: dict[str, str] = {}
    for key in initial:
        new[initial[key]] = key
    return new


def favorite_color(favorites: dict[str, str]) -> str:
    """Return the most fequent color."""
    ending: list = []
    for key in favorites:
        ending.append(favorites[key])
    return max(ending, key=ending.count)


def count(keys: list[str]) -> dict[str, int]:
    """Make a dictionary with the keys as list values and values as frequency."""
    final: dict[str, int] = {}
    for key in keys:
        if key in final:
            final[key] += 1
        else:
            final[key] = 1
    return final