"""
Puzzle 05:

Implement a mod function without using the operator.
"""


def mod(a, b):
    while a >= b:
        a -= b
    return a


def mod_recursive(a, b):
    if a < b:
        return a
    return mod_recursive(a - b, b)


if __name__ == "__main__":

    print(mod(10, 3))
    print(mod_recursive(10, 3))
