"""Ex05 - Lists -"""

__author__ = 730489294


def only_evens(values: list[int]) -> list[int]:
    """This function takes in a list of integers and returns a list of the even ints."""
    new_list: list = list()
    i: int = 0
    while i < len(values):
        quotient: int = 0
        quotient = values[i] % 2
        if quotient == 0:
            new_list.append(values[i])
        i += 1

    return new_list


def sub(values: list[int], a: int, b: int) -> list[int]:
    """This function takes in a list of integers and two index values and returns a list of the index values."""
    new_list: list = list()
    new_list.append(values[a])
    new_list.append(values[b])
    return new_list


def concat(values: list[int], integer: list[int]) -> list[int]:
    """This function concatenates two lists together and returns that list."""
    new_list: list = list()
    i: int = 0
    j: int = 0
    while i < len(values):
        new_list.append(values[i])
        i += 1
    
    while j < len(integer):
        new_list.append(integer[j])
        j += 1

    return new_list
