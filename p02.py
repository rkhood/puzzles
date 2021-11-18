"""
Puzzle 02:

Given a list as input with one duplicate, find the duplicate.
"""


def find_duplicate(lst):

    dup = {}
    for val in lst:
        if val in dup:
            return val
        dup[val] = 1


if __name__ == "__main__":

    print(find_duplicate([1, 10, 15, 2, 7, 8, 7]))
