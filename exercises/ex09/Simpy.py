"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union


__author__ = "730489294"


class Simpy:
    """Functions for numerical operations."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initilize Simpy with its values."""
        self.values = values

    def __str__(self) -> str:
        """Produce a string representation of Simpy."""
        return f"Simpy({self.values})"

    def fill(self, fill_val: float, times: int) -> None:
        """Fills in numbers for values list."""
        self.values = []
        i = 0
        while i < times:
            self.values.append(fill_val)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """This function fills in the values attributes sith range of values."""
        assert step != 0.0
       
        if step > 0.0:
            while start < stop:
                self.values.append(start)
                start += step
        elif step < 0.0:
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Adds all the items in the values attribute."""
        total: float = 0.0
        for item in self.values:
            total += item

        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Allows you to use the add operator with Simpy and floats."""
        new_val: list[float] = []

        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_val.append(self.values[i] + rhs.values[i])
        else:
            for item in self.values:
                new_val.append(item + rhs)
     
        return Simpy(new_val)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Allows you to use the power operator with Simpy and floats."""
        new_val: list[float] = []

        if isinstance(rhs, Simpy):
            # assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                new_val.append(self.values[i] ** rhs.values[i])
        else:
            for item in self.values:
                new_val.append(item ** rhs)

        return Simpy(new_val)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Allows you to test if values are equal."""
        answer: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    answer.append(True)
                else:
                    answer.append(False)    
        else:
            for item in self.values:
                if item == rhs:
                    answer.append(True)
                else:
                    answer.append(False)
    
        return answer

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Allows you to test if a value is greater than another set of values."""
        answer: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    answer.append(True)
                else:
                    answer.append(False)    
        else:
            for item in self.values:
                if float(item) > rhs:
                    answer.append(True)
                else:
                    answer.append(False)
    
        return answer

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """This allows you to use subscription notation."""
        number: float = 0.0
        answer: list[float] = []
        if isinstance(rhs, int):
            i = 0
            for item in self.values:
                if i == rhs:
                    number = float(item)
                i += 1
            return number
        else:
            assert len(self.values) == len(rhs)
            i = 0
            for item in self.values:
                if rhs[i]:
                    answer.append(item)
                i += 1
            return Simpy(answer)
    
