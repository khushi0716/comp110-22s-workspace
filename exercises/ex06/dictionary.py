"""Ex06 Dictionary Functions."""

__author__ = "730489294"

dictio = {"UNC": "Thing", "Duke": "Duke", "State": "Farm"}
colors = {"Mark": "yellow", "Pete": "blue", "Matt": "blue", "Bill": "yellow"}


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and inverts the keys and values."""
    invert_things: dict[str, str] = dict()
 
    for key in dictionary:
        answer = dictionary[key]
        for index in invert_things:
            if answer == index:
                raise KeyError("You can't have the same key.")
        
        invert_things[dictionary[key]] = key
    
    return invert_things


print(invert(dictio))


def favorite_color(dict_a: dict[str, str]) -> str:
    """Takes a dictionary with colors as valus and returns the most frequent color."""
    frequency_dict: dict[str, int] = dict()
    for item in dict_a:
        color = dict_a[item]
        if color not in frequency_dict:
            frequency_dict[color] = 1
        else:
            frequency_dict[color] += 1
    max: int = 0
    answer: str = ""
    for color in frequency_dict:
        if frequency_dict[color] > max:
            max = frequency_dict[color]
            answer = color

    return answer


def count(a: list[str]) -> dict[str, int]:
    """Takes a list of stirngs and stores it in a dictionary with strings as key and frequency as value."""
    diction: dict[str, int] = dict()
    i: int = 0
    while i < len(a):
        if a[i] not in diction:
            diction[a[i]] = 1
        else:
            diction[a[i]] += 1
        i += 1
    return diction
