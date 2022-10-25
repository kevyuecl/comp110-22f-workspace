"""EX05- List Utility Functions (tests version)."""
__author__ = "730559522"


from utils import only_evens, sub, concat


def test_only_evens_no_item() -> None:
    """Tests list with no items."""
    int_list: list[int] = []
    assert only_evens(int_list) == []


def test_only_evens_first_integer_combination() -> None:
    """Tests list with a combination of even and odd integers."""
    int_list: list[int] = [1, 2, 4, 5]
    assert only_evens(int_list) == [2, 4]


def test_only_evens_second_integer_combination() -> None:
    """Tests list with another combination of even and odd integers."""
    int_list: list[int] = [3, 6, 8, 11]
    assert only_evens(int_list) == [6, 8]


def test_concat_no_item() -> None:
    """Tests list with no items."""
    int_list_one: list[int] = []
    int_list_two: list[int] = []
    assert concat(int_list_one, int_list_two) == []


def test_concat_use1() -> None:
    """Tests list use cases of the same length."""
    int_list_one: list[int] = [1, 3, 5]
    int_list_two: list[int] = [2, 4, 6]
    assert concat(int_list_one, int_list_two) == [1, 3, 5, 2, 4, 6]


def test_concat_use2() -> None:
    """Tests list use cases of different lengths."""
    int_list_one: list[int] = [1, 3, 5]
    int_list_two: list[int] = [7, 9]
    assert concat(int_list_one, int_list_two) == [1, 3, 5, 7, 9]


def test_sub_no_item() -> None:
    """Tests list with no items."""
    inputed_list: list[int] = []
    start_index = 0
    end_index = 3
    assert sub(inputed_list, start_index, end_index) == []


def test_sub_use1() -> None:
    """Tests list that is expected based on start and end indices."""
    inputed_list: list[int] = [3, 4, 5, 6]
    start_index = 0
    end_index = 2
    assert sub(inputed_list, start_index, end_index) == [3, 4]


def test_sub_use2() -> None:
    """Test list that is expected based on start and end indices for another set of integers."""
    inputed_list: list[int] = [5, 7, 3, 6, 1]
    start_index = 1
    end_index = 3
    assert sub(inputed_list, start_index, end_index) == [7, 3]