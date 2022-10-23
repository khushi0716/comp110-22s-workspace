def reverse_list(a: list[str]) -> list[str]:
    new_list: list[str] = []
    i = len(a) - 1
    while i >= 0:
        if len(a[i]) >= 3:
            new_list.append(a[i])
        i -= 1
    return new_list


listtt = ["a", "bb", "ccc", "dddd", "eeeee"]


# print(reverse_list(listtt))


thing: dict[str, list[float]] = {"high": [78.0, 90.0, 76], "low": [45.0, 56.0, 65.0], "wind": [15.0, 10.0, 12.0]}


def average(place: dict[str, list[float]], index: int) -> float:
    high = place["high"][index]
    low = place["low"][index]
    average = (high + low) / 2

    return average 


# print(average(thing, 0))

thingg: str = "hell o ll"


def streak(word: str) -> str:
    long_s: str = " "
