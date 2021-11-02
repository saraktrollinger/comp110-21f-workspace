"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730393060"


from exercises.ex06.dictionaries import invert
from exercises.ex06.dictionaries import favorite_color
from exercises.ex06.dictionaries import count


def test_invert() -> None:
    """Invert a dictionary."""
    initial = {"Hi": "Bye", "Good": "Bad", "Red": "Green"}
    new = invert(initial)
    assert new == {"Bye": "Hi", "Bad": "Good", "Green": "Red"}


def test_invert_key_error() -> None:
    """Invert a dictionary but have two of the same values."""
    initial = {"Hi": "Bye", "Good": "Bad", "Happy": "Bad"}
    new = invert(initial)
    assert new == KeyError


def test_invert_short() -> None:
    """Invert dictionary but have two of the same keys."""
    initial = {"Hi": "Bye", "Sad": "Happy"}
    new = invert(initial)
    assert new == {"Bye": "Hi", "Happy": "Sad"}


def test_favorite_color() -> None:
    """Most popular name is returned from a dictionary."""
    favorites = {"SK": "Purple", "Avery": "Blue", "Judy": "Blue", "Grace": "Yellow"}
    ending = favorite_color(favorites)
    assert ending == "Blue"


def test_favorite_color_equal() -> None:
    """Most popular color returned but there is a tie between colors."""
    favorites = {"SK": "Purple", "Avery": "Blue", "Judy": "Blue", "Grace": "Purple"}
    ending = favorite_color(favorites)
    assert ending == "Purple"


def test_favorite_color_single() -> None:
    """Most popular color returned but there's only one color."""
    favorites = {"SK": "Purple", "Grace": "Purple"}
    ending = favorite_color(favorites)
    assert ending == "Purple"


def test_count() -> None:
    """Return list values as key values in a dict and assign frequency as their value."""
    keys = ["Hello", "Goodbye", "Hello", "Howdy", "Greetings"]
    final = count(keys)
    assert final == {"Hello": 2, "Goodbye": 1, "Howdy": 1, "Greetings": 1}


def test_count_empty() -> None:
    """Return a dictionary with keys as list items and value as frequency but with an empty list."""
    keys = []
    final = count(keys)
    assert final == {}


def test_count_same() -> None:
    """Return a dictionary with keys as list items and frequency as value but the list has the same values."""
    keys = ["Hello", "Hello", "Hello"]
    final = count(keys)
    assert final == {"Hello": 3}