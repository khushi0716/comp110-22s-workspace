"""Ex05 - Lists Test -"""

__author__ = 730489294


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests an empty list to see that it gives you an empty list back."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_even_item() -> None:
    """Tests a list of one even item to see if it returns that single even item."""
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_single_odd_item() -> None:
    """Tests a list of one odd item to see if it will give an empty list back."""
    xs: list[int] = [3]
    assert only_evens(xs) == []


def test_only_evens_many_items() -> None:
    """Tests a list of several items to see if it will give a list of even ints back."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert only_evens(xs) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def test_only_evens_all_odd_items() -> None:
    """Tests a list of just odd values to see if it will give an empty list."""
    xs: list[int] = [1, 3, 5, 7, 9, 11]
    assert only_evens(xs) == []


def test_only_evens_all_even_items() -> None:
    """Tests a list of just even values to see if it will return the same list."""
    xs: list[int] = [2, 4, 6, 8, 10, 12]
    assert only_evens(xs) == [2, 4, 6, 8, 10, 12]


def test_sub_same_index() -> None:
    """Tests when indexes are the same to see if it will return a list of two of the same value."""
    xs: list[int] = [1, 3, 5]
    assert sub(xs, 1, 1) == [3, 3]


def test_sub_last_two_indexes() -> None:
    """Tests to see if it will return a list of the last two int values."""
    xs: list[int] = [1, 3, 5]
    assert sub(xs, (len(xs) - 2), len(xs) - 1) == [3, 5]


def test_sub_first_two_indexes() -> None:
    """Tests to see if it will return a list of the first two int values."""
    xs: list[int] = [1, 3, 5]
    assert sub(xs, 0, 1) == [1, 3]


def test_sub_higher_index_before_lower_index() -> None:
    """Tests to see if it will return a list when index "a" is larger than index "b"."""
    xs: list[int] = [3, 2, 6, 5, 4, 5]
    assert sub(xs, 4, 2) == [4, 6]


def test_concat_empty_lists() -> None:
    """Tests to see if two empty lists will return an empty list."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_one_list_is_empty() -> None:
    """Tests to see if concatenating an empty list and a list that it will return the list."""
    xs: list[int] = []
    ys: list[int] = [2, 3, 5, 6, 3]
    assert concat(xs, ys) == [2, 3, 5, 6, 3]


def test_concat_two_same_size_lists() -> None:
    """Tests to see if it will return a list when the two lists are the same length."""
    xs: list[int] = [1, 3, 4, 3, 6]
    ys: list[int] = [2, 3, 2, 2, 1]
    assert concat(xs, ys) == [1, 3, 4, 3, 6, 2, 3, 2, 2, 1]


def test_concat_two_different_size_lists() -> None:
    """Tests to see if it will return a list when the two lists are different lengths."""
    xs: list[int] = [1, 3, 4, 3, 6]
    ys: list[int] = [2, 3]
    assert concat(xs, ys) == [1, 3, 4, 3, 6, 2, 3]
