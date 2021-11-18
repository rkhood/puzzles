"""
Puzzle 03:

Given a list as input that contains pairs and one unique number,
find the unique number.

xor properties:
    1. a ^ a = 0
    2. (a ^ b) ^ c = a ^ (b ^ c)
    3. a ^ 0 = a

so, a ^ a ^ b ^ b ^ c = c
"""


def reduce(func, lst, initial=0):

    collector = initial
    for item in lst:
        collector = func(collector, item)
    return collector


def find_unique(lst):
    xor = lambda a, b: a ^ b
    return reduce(xor, lst)


if __name__ == "__main__":

    print(find_unique([1, 3, 4, 3, 1, 2, 2]))
