"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730393060"


def test_only_evens_empty() -> None:
    list_one: list[int] = []
    assert only_evens(list_one) == []


def test_only_evens_single_item() -> None:
    list_one: list[int] = [4]
    assert only_evens(list_one) == [4]


def test_only_evens_many_items() -> None:
    list_one: list[int] = [3, 8, 7, 2]
    assert only_evens(list_one) == [8, 2]


def test_sub_empty() -> None:
    initial: list[int] = []
    start: int = 0
    end: int = 0
    assert sub(initial, start, end) == []


def test_sub_single_item() -> None:
    initial: list[int] = [4, 5, 6, 7]
    start: int = 4
    end: int = 5
    assert sub(initial, start, end) == [4]


def test_sub_many_items() -> None:
    initial: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start: int = 3
    end: int = 11
    assert sub(initial, start, end) == [3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_empty() -> None:
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_concat_single_item() -> None:
    list_one: list[int] = [1]
    list_two: list[int] = [4]
    assert concat(list_one, list_two) == [1, 4]


def test_concat_many_items() -> None:
    list_one: list[int] = [4, 6, 19]
    list_two: list[int] = [6, 7, 3]
    assert concat(list_one, list_two) == [4, 6, 19, 6, 7, 3]