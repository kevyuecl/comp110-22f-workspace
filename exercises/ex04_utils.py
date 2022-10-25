"""EX04- List Util."""
__author__ = "730559522"


def all(int_list: list[int], num: int) -> bool:
    """Indicates whether all numbers in list match the indicated number."""
    ind: int = 0
    if len(int_list) == 0:
        return False
    # Return false if the list is empty
    while ind < len(int_list):
        if (num == int_list[ind]):
            ind += 1
        else: 
            return False
    return True
    # Each element of the list is checked on whether they match the given number


def max(int_list: list[int]) -> int:
    """Returns maximum value in the list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    ind: int = 0
    max_num: int = int_list[ind]
    # When list is empty, raise an error

    while ind < len(int_list):
        if max_num < int_list[ind]:
            max_num = int_list[ind]
        ind += 1
    return max_num
    # Each element of the list is compared to the previously set max value. The max value is returned. 


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Checks whether the two lists have deep equality."""
    ind: int = 0
    if len(first_list) == len(second_list):
        while ind < len(first_list):
            if (first_list[ind] == second_list[ind]):
                ind += 1
            else: 
                return False  # No deep equality
        return True
        # Deep equality
    return False
    # List lengths are not the same, therefore no deep equality