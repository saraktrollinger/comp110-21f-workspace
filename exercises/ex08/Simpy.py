"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730393060"


class Simpy:
    """Utility class initialization."""
    values: list[float]

    def __init__(self, values: list[float]):
        """New Simpy object initialization."""
        self.values = values

    def __str__(self) -> str:
        """A string representation of Simpy."""
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        """Fill values with specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < y:
            self.values.append(x)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill the values attributes in terms of floats."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            other_value: float = start
            while other_value < stop:
                self.values.append(other_value)
                other_value += step
        if step < 0.0:
            other_value: float = start
            while other_value > stop:
                self.values.append(other_value)
                other_value += step
    
    def sum(self) -> float:
        """Compute and return the sum of all value items."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        ending: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                ending.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            for x in self.values:
                ending.values.append(x + rhs)
        return ending

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for multiplication."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            for x in self.values:
                result.values.append(x ** rhs)
        return result
    
    def __eg__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for equality."""
        final: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                final.append(self.values[i] == rhs.values[i])
                i += 1
        else:
            for x in self.values:
                final.append(x == rhs)
        return final

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for greater than."""
        end: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                end.append(self.values[i] > rhs.values[i])
                i += 1
        else:
            for x in self.values:
                end.append(x > rhs)
        return end

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Read specific items from the simpy array."""
        fin: Simpy = Simpy([])
        if isinstance(rhs, int):
            return float(self.values[rhs])
        else:
            assert len(self.values) == len(rhs)
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    fin.values.append(self.values[i])
                i += 1
            return fin