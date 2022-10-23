def reverse_multiply(a: list[int]) -> list[int]:
    new: list[int] = []
    i = len(a) - 1
    while i >= 0:
        new.append(a[i] * 2)
        i -= 1
    return new


# reverse_multiply([5, 10, 15])


def free_biscuits(d: dict[str, list[int]]) -> dict[str, bool]:
    new_dict: dict[str, bool] = {}
    
    for game in d:
        points: int = 0
        for value in d[game]:
            points += value
        
        if points >= 100:
            new_dict[game] = True
        else: 
            new_dict[game] = False

    return new_dict


def merge_lists(word: list[str], num: list[int]) -> dict[str, int]:
    merger: dict[str, int] = {}
    if len(word) != len(num):
        return merger
    else:
        i = 0
        while i < len(word):
            merger[word[i]] = num[i]
            i += 1
        return merger


class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int) -> None:
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int):
        self.marshmallow_count += mallows
        self.sweetness += mallows * 2

    def calorie_count(self) -> float:
        count: float = 0.0
        if self.flavor == "vanilla" or "peppermint":
            count += 30
        else:
            count += 20

        if self.has_whip:
            count += 100
        
        count += self.marshmallow_count / 2

        return count


class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int) -> None:
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, num: int) -> None:
        self.minutes += num

    def reset(self) -> int:
        new_min: int = self.minutes
        self.minutes = 0
        return new_min

    def report(self) -> None:
        min: int = self.minutes % 60
        hrs: int = self.minutes // 60
        print(f"{self.name} has spent {hrs} and {min} on {self.purpose}.")