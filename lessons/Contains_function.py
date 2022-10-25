"""Example implementing a list utility function."""

# Function name: contains
# we will have 2 parameters: needle (str), haystack (list[str])
#Return value of function: True if the needle is found in the haystack at least once. False otherwise
#Gameplan:
# 1. Start with the first index
# 2. Loop through every index
#  2.A Test if item at index equal to needle
#  2.A True Return True! We foudn it!
# 3. Return False

def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if (haystack[i] == needle):
            return True
        i += 1
    return False
