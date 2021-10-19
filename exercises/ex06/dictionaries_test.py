"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730330727"

from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert_use_1() -> None:
    """Tests the first use case."""
    A: dict[str, str] = {"apple": "blue", "banana": "yellow"}
    assert invert(A) == {"blue": "apple", "yellow": "banana"}


def test_invert_use_2() -> None:
    """Tests second use case."""
    A: dict[str, str] = {"apple": "blue"}
    assert invert(A) == {"blue": "apple"}


def test_invert_edge() -> None:
    """Tests edge case."""
    A: dict[str, str] = {"apple": ""}
    assert invert(A) == {"": "apple"}


def test_favorite_color_use_1() -> None:
    """Tests first use case."""
    A: dict[str, str] = {"apple": "blue", "banana": "yellow", "peach": "yellow"}
    assert favorite_color(A) == "yellow"


def test_favorite_color_use_2() -> None:
    """Tests second use case."""
    A: dict[str, str] = {"apple": "blue", "banana": "yellow", "peach": "blue"}
    assert favorite_color(A) == "blue"


def test_favorite_color_edge() -> None:
    """Tests edge use case."""
    A: dict[str, str] = {"apple": "blue"}
    assert favorite_color(A) == "blue"


def test_count_use_1() -> None:
    """Tests first use case."""
    A: list[str] = ["a", "a", "h", "h", "h", "h", "h", "h", "h", "g", "f", "e", "d", "a", "d", "c", "b"]
    assert count(A) == {'a': 3, 'h': 7, 'g': 1, 'f': 1, 'e': 1, 'd': 2, 'c': 1, 'b': 1}


def test_count_use_2() -> None:
    """Tests first use case."""
    A: list[str] = ["a", "a", "h", "h"]
    assert count(A) == {'a': 2, 'h': 2}


def test_count_edge() -> None:
    """Tests edge use case."""
    A: list[str] = [""]
    assert count(A) == {'': 1}