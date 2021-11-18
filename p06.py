"""
Puzzle 06:

Take an int as input and represent it as a binary string.
"""


def binary(val):

    if val == 0:
        return "0"
    return binary(val // 2) + str(val % 2)


if __name__ == "__main__":

    print(binary(11))
