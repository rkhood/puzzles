"""
Puzzle 00:

Make a 9 digit number from 1-9 using all numbers such that the first
digit is divisible by 1, the first 2 digits are divisible by 2 etc.
"""

from itertools import permutations
from typing import List


Num = int
Sequence = List[str]


def sequence(sequence: Sequence) -> Sequence:
    return ["".join(p) for p in permutations(sequence)]


def divisible(num: Num, div: Num) -> bool:
    return num % div == 0


def find_number_order(sequence: Sequence):
    divs = range(2, 10)
    for seq in sequence:
        for div in divs:
            if not divisible(int(seq[:div]), div):
                break
            if div == 9:
                print(seq)


if __name__ == "__main__":

    seq = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    find_number_order(sequence(seq))
