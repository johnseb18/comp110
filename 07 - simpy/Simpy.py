"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730612873"


class Simpy:
    """Class."""
    values: list[float]
    
    def __init__(self, ones: list[float]):
        """Initializes the values attribute of the Simpy object to the argument passed in."""
        self.values = ones

    def __repr__(self) -> str:
        """Called whenever a Simpy object is converted to a str."""
        return f"Simpy({self.values})"

    def fill(self, twos: float, mixed: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        i: int = 0
        self.values = []
        while i < mixed:
            self.values.append(twos)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Fills in the values attribute with range of values in terms of floats."""
        assert step != 0.0
        self.values = []
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        if step < 0.0:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute."""
        result: float = sum(self.values)
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Adds each index of two lists together."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)  
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i += 1
        return result

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Takes each index of one list to the power of the same index of another list."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i]) 
        else:
            for item in self.values:
                result.values.append(item ** rhs)
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Ability to produce a mask based on the equality of each item in values and some other Simpy object of float value."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            while i < len(self.values):
                if rhs.values[i] == self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if rhs == self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Ability to produce a mask based on the greater than relationship between each item in values with some other Simpy object or float value."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            while i < len(self.values):
                if rhs.values[i] < self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if rhs < self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Ability to use the subscription operator with Simpy objects."""
        result_1: float = 0
        if isinstance(rhs, int):
            i: int = 0
            while i < len(self.values):
                if rhs == i:
                    result_1 = self.values[i]
                i += 1
            return result_1
        else:
            result_2: Simpy = Simpy([])
            i: int = 0
            while i < len(rhs):
                if rhs[i] is True:
                    result_2.values.append(self.values[i])
                i += 1
            return result_2

    