"""Creating functions and testing utility functions."""


__author__ = "730612873"


def only_evens(x: list[int]) -> list[int]:
    """Returning the evens in the list."""
    evens: list[int] = []
    for num in x:
        if num % 2 == 0:
            evens.append(num)
    return evens


def concat(x: list[int], y: list[int]) -> list[int]:
    """Combining two lists."""
    combine: list[int] = []
    for num in x:
        combine.append(num)
    for nums in y:
        combine.append(nums)
    return combine


def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """Generate a sublist."""
    if x < 0:
        x = 0
    if y >= len(a_list):
        y = len(a_list)
    if len(a_list) == 0 or x > len(a_list) or y < 1:
        return []
    n_list: list[int] = []
    while x < y:
        n_list.append(a_list[x])
        x += 1
    return n_list