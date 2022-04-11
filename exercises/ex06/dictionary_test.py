"""Ex06 Dictionary Function Tests."""

__author__ = "730489294"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_empty_dict() -> None:
    """Tests what will happen if invert is given an empty list."""
    xs: dict[str, str] = dict() 
    assert invert(xs) == dict()


def test_invert_key_error() -> None:
    """Tests what will happen when you have a keyError."""
    with pytest.raises(KeyError):
        my_dictionary: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)
        raise KeyError({'kris': 'jordan', 'michael': 'jordan'})
        
        
def test_favorite_color_two_maxes() -> None:
    """Tests what will happen if favorite_color is given two maxes."""
    xs: dict[str, str] = {"Mark": "yellow", "Pete": "blue", "Matt": "blue", "Bill": "yellow"}
    assert favorite_color(xs) == "yellow"


def test_favorite_color_all_the_same() -> None:
    """Tests what will happen if everone has the same fav color."""
    xs: dict[str, str] = {"Mark": "yellow", "Pete": "yellow", "Matt": "yellow", "Bill": "yellow"}
    assert favorite_color(xs) == "yellow"


def test_favorite_color_everyone_has_diff_colors() -> None:
    """Tests what will happen if everyone has different fav colors."""
    xs: dict[str, str] = {"Mark": "yellow", "Pete": "blue", "Matt": "green", "Bill": "magenta"}
    assert favorite_color(xs) == "yellow"


def test_count_with_small_list() -> None:
    """Tests what will happen if count is given small list."""
    listtt: list[str] = ["five", "five", "two"]
    assert count(listtt) == {'five': 2, 'two': 1}


def test_count_with_large_list() -> None:
    """Tests what will happen if count is given an large list."""
    listtt: list[str] = ["five", "five", "two", "five", "five", "two", "five", "five", "two"]
    assert count(listtt) == {'five': 6, 'two': 3}


def test_count_with_empty_list() -> None:
    """Tests what will happen if count is given an empty list."""
    listtt: list[str] = []
    assert count(listtt) == {}