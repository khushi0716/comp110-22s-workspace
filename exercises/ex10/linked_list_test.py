"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, is_equal, scale


__author__ = "730489294"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value_at of an enpty list should raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 2)


def test_value_at_index_out_of_bounds() -> None:
    """Value_at with an index greater than the length of the list should raise an IndexError."""
    with pytest.raises(IndexError):
        linked_list = Node(1, Node(2, Node(3, None)))
        assert value_at(linked_list, 5)


def test_value_at_non_empty() -> None:
    """Value_at should return the the data at the inputted index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_max_empty() -> None:
    """Max of an empty list should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_non_empty() -> None:
    """Max of a non empty list should return the maximum value of the list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_linkify_non_empty() -> None:
    """Linkify of a non empty list should make a linked list of Nodes."""
    linked_list = [1, 2, 3]
    assert is_equal(linkify(linked_list), Node(1, Node(2, Node(3, None))))


def test_linkify_empty() -> None:
    """Linkify of an empty list should return None."""
    linked_list = []
    assert is_equal(linkify(linked_list), None)


def test_scale_non_empty() -> None:
    """Scale of a non empty list should scale the node.data values by the factor given."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(scale(linked_list, 2), Node(2, Node(4, Node(6, None))))


def test_scale_empty() -> None:
    """Scale of an empty list should return None."""
    linked_list = None
    assert is_equal(scale(linked_list, 2), None)


def test_scale_one_node() -> None:
    """Scale of one Node should return the one node.data value scaled by the factor."""
    linked_list = Node(1, None)
    assert is_equal(scale(linked_list, 2), Node(2, None))
