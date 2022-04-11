"""Ex08 related utility functions."""

__author__ = "730489294"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def head(header: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}

    for column in header:
        empty_list = []
        i: int = 0
        if number >= len(header[column]):
            number = len(header[column])
        
        while i < number:
            empty_list.append(header[column][i])
            i += 1
        result[column] = empty_list
 
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in names:
        result[item] = table[item]

    return result


def count(frequency: list[str]) -> dict[str, int]:
    """Produces a dict where each key is a unique value in a list and each value  is the count of times that value is in the list."""
    result: dict[str, int] = {}
    for item in frequency:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result