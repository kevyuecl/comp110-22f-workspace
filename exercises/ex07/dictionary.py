"""EX07- Dictionary Functions."""
__author__ = "730559522"


def invert(start_dict: dict[str, str]) -> dict[str, str]:
    """Inverts key-value pairs of dictionary and raises error when dupe keys arise."""
    reverse_dict: dict[str, str] = {}
    for key in start_dict:
        value = start_dict[key]
        reverse_dict[value] = key
    if len(reverse_dict) != len(start_dict):
        raise KeyError
    else:
        return reverse_dict


def count(init_list: list[str]) -> dict[str, int]:
    """Produces dictionary with info regarding the number of time each list item appears."""
    num_elems: dict[str, int] = {}
    for key in init_list:
        if key in num_elems:
            num_elems[key] += 1
        else:
            num_elems[key] = 1
    return num_elems


def favorite_color(colors: dict[str, str]) -> str:
    """Returns most prevalent color from given dictionary as a string."""
    color_list: list[str] = []
    for color in colors:
        color_list.append(colors[color])
    commonality: dict[str, int] = count(color_list)
    most_common: int = 0
    favoritecol: str = ""
    for color in commonality:
        if commonality[color] > most_common:
            most_common = commonality[color]
            favoritecol = color
    return favoritecol