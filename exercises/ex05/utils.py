"""EX05- List Utility Functions (Implementation)."""
__author__ = "730559522"


def only_evens(int_list: list[int]) -> list[int]:
    """Returns only even integers from the list."""
    i: int = 0
    even_num_list: list[int] = []
    while (i < len(int_list)):
        if int_list[i] % 2 == 0:
            even_num_list.append(int_list[i])
            i += 1
        else:
            i += 1
    return even_num_list


def concat(int_list_one: list[int], int_list_two: list[int]) -> list[int]:
    """Returns list containing all elements of 1st list followed ay all elements of 2nd list."""
    list_concatenated: list[int] = []
    first_index: int = 0
    second_index: int = 0
    while (first_index < len(int_list_one)):
        list_concatenated.append(int_list_one[first_index])
        first_index += 1
    while (second_index < len(int_list_two)):
        list_concatenated.append(int_list_two[second_index])
        second_index += 1
    return list_concatenated


def sub(inputed_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns list that is subset of given list, between start index and end index - 1."""
    subset_list: list[int] = []
    if len(inputed_list) == 0 and start_index > len(inputed_list) or end_index <= 0:
        return subset_list
    elif end_index > len(inputed_list):
        end_index = len(inputed_list)
    elif start_index < 0:
        start_index = 0
    while (start_index < end_index):
        subset_list.append(inputed_list[start_index])
        start_index += 1
    return subset_list