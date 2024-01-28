"""Something with test utils."""

__author__ = "730612873"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Testing only_evens with an empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_single_item() -> None:
    """Testing only_evens with a single item."""
    x: list[int] = [1]
    assert only_evens(x) == []


def test_only_evens_many_items() -> None:
    """Testing only_evens with many items."""
    x: list[int] = [2, 3, 5, 6]
    assert only_evens(x) == [2, 6] 


def test_concat_empty() -> None:
    """Testing concat with empty lists."""
    x: list[int] = [] 
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_single_item() -> None:
    """Testing concat with single items."""
    x: list[int] = [1] 
    y: list[int] = [2]
    assert concat(x, y) == [1, 2]


def test_concat_many_items() -> None:
    """Testing concat with many items."""
    x: list[int] = [1, 2, 3] 
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]


def test_sub_empty() -> None:
    """Testing sub with an empty set."""
    a_list: list[int] = []
    x: int = 0 
    y: int = 0
    assert sub(a_list, x, y) == []


def test_sub_single_item() -> None:
    """Testing sub with a single items."""
    a_list: list[int] = [10]
    x: int = 1 
    y: int = 2
    assert sub(a_list, x, y) == []


def test_sub_many_items() -> None:
    """Testing sub with many items."""
    a_list: list[int] = [10, 20, 30, 40]
    x: int = 1 
    y: int = 3
    assert sub(a_list, x, y) == [20, 30]