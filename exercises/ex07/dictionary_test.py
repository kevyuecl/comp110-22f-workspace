"""Dictionary Test Functions."""
__author__ = "730559522"


import pytest
from dictionary import invert, count, favorite_color


def test_invert_empty() -> None:
    """Test invert empty dictionary."""
    provided_dict: dict[str, str] = {}
    assert invert(provided_dict) == {}


def test_invert_use1() -> None:
    """Test invert use case."""
    provided_dict: dict[str, str] = {"UNC": "Dukie"}
    assert invert(provided_dict) == {"Dukie": "UNC"}


def test_invert_use2() -> None:
    """Test invert use case."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_count_empty() -> None:
    """Test count empty list."""
    provided_list: list[str] = []
    assert count(provided_list) == {}


def test_count_use1() -> None:
    """Test count use case."""
    provided_list: list[str] = ["1", "1", "1", "2", "2", "3"]
    assert count(provided_list) == {'1': 3, '2': 2, '3': 1}


def test_count_use2() -> None:
    """Test count use case."""
    provided_list: list[str] = ["Duck", "Duck", "Goose"]
    assert count(provided_list) == {'Duck': 2, 'Goose': 1}


def favorite_color_empty() -> None:
    """Test for favorite_color empty dictionary."""
    provided_dict: dict[str, str] = {}
    assert favorite_color(provided_dict) == ""


def favorite_color_use1() -> None:
    """Test for favorite_color use case."""
    provided_dict: dict[str, str] = {"Alan": "yellow", "Kevin": "blue", "Kris": "blue"}
    assert favorite_color(provided_dict) == "blue"


def favorite_color_use2() -> None:
    """Test for favorite_color use case."""
    provided_dict: dict[str, str] = {"Alan": "yellow", "Kevin": "blue"}
    assert favorite_color(provided_dict) == "yellow"