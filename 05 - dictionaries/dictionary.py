"""Practicing with dictionaries."""


__author__ = "730612873"


def invert(before: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values in a dictionary."""
    result: dict[str, str] = {}
    for key in before:
        i = before[key]
        result[i] = key
        for a in before:
            if before[key] == before[a] and key != a:
                raise KeyError("There can't be duplicate keys in a dictionary!")
    return result


def favorite_color(colors: dict[str, str]) -> str():
    """Returns a favorite color that appears the most frequently."""
    new_colors: dict = {}
    result: str = ""
    for key in colors:
        print(key)
        if colors[key] in new_colors:
            new_colors[colors[key]] += 1
        else:
            new_colors[colors[key]] = 1
    i: int = 0
    for key in new_colors:
        if new_colors[key] > i:
            i = new_colors[key]
            result = key
    return result


def count(input: list[str]) -> dict[str, int]:
    """Counting how many times a value appears in the input list."""
    result = {}
    for key in input:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result