"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_even() -> None:
    """Tests only evens."""
    A: list[int] = [2, 2, 2]
    assert only_evens(A) == [2, 2, 2]


def test_only_evens_odd() -> None:
    """Tests only odds."""
    A: list[int] = [1, 1, 1]
    assert only_evens(A) == []


def test_only_evens_empty() -> None:
    """Tests an empty list."""
    A: list[int] = []
    assert only_evens(A) == []


def test_sub_3_items() -> None:
    """Tests for 3 items in output."""
    a: list[int] = [1, 2, 3, 4, 5]
    i: int = 1
    j: int = 4
    assert sub(a, i, j) == [2, 3, 4]


def test_sub_same_index() -> None:
    """Tests for the index being the same."""
    a: list[int] = [1, 2, 3, 4, 5]
    i: int = 2
    j: int = 2
    assert sub(a, i, j) == []


def test_sub_same_array() -> None:
    """Tests for an array of all the same number."""
    a: list[int] = [1, 1, 1, 1, 1, 1]
    i: int = 1
    j: int = 6
    assert sub(a, i, j) == [1, 1, 1, 1, 1]


def test_concat_4_items() -> None:
    """Tests an output of four items."""
    a: list[int] = [1, 1]
    b: list[int] = [1, 1]
    assert concat(a, b) == [1, 1, 1, 1]


def test_concat_diff_lengths() -> None:
    """Tests for lists of different lengths."""
    a: list[int] = [1, 1, 1]
    b: list[int] = [1]
    assert concat(a, b) == [1, 1, 1, 1]


def test_concat_blank_list() -> None:
    """Tests for concating a blank list."""
    a: list[int] = []
    b: list[int] = [1, 1, 1, 1]
    assert concat(a, b) == [1, 1, 1, 1]