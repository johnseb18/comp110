"""Testing the functions in dictionary."""

__author__ = "730612873"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def invert_empty() -> None:
    """Testing invert with an empty dictionary."""
    before: dict[str, str] = {}
    assert invert(before) == {}


def invert_single() -> None:
    """Testing invert with a single item."""
    before: dict[str, str] = {'a': 'z'}
    assert invert(before) == {'z': 'a'}


def invert_many() -> None:
    """Testing invert with many items."""
    before: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(before) == {'z': 'a', 'y': 'b', 'x': 'c'}


def favorite_color_empty() -> None:
    """Testing favorite_color with an empty dictionary."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ()


def favorite_color_single() -> None:
    """Testing favorite_color with a single item."""
    colors: dict[str, str] = {"Marc": "yellow"}
    assert favorite_color(colors) == "yellow"


def favorite_color_many() -> None:
    """Testing favorite_color with many items."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def count_empty() -> None:
    """Testing count with an empty list."""
    input: list[str] = []
    assert count(input) == {}


def count_single() -> None:
    """Testing count with a single item."""
    input: list[str] = ["yellow"]
    assert count(input) == {"yellow": 1}


def count_many() -> None:
    """Testing count with many items."""
    input: list[str] = ["yellow", "yellow", "blue"]
    assert count(input) == {'yellow': 2, 'blue': 1}