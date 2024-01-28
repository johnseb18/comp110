"""Creating functions that compare lists and find the largest integer in a list."""


__author__ = "730612873"



def all(list1: list[int], x: int) -> bool:
    for value in list1:
        if value != x:
            return False
        
    return True

def max(list1: list[int]) -> int:
    max: int = 0
    if len(list1) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        for value in list1:
            if value > max:
                max = value
                
        
    return max

def is_equal(list1: list[int], list2: list[int]) -> bool:
    i: int = 0
    if len(list1) != len(list2):
        return False
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
        
    return True