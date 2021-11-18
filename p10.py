"""
Puzzle 10:

Implement a dictionary.

Methods: add, lookup.
"""


class Dict:
    def __init__(self, num=1000):
        self.dictionary = [[] for i in range(num)]
        self.num = num

    def add(self, key, val):
        idx = hash(key) % self.num
        self.dictionary[idx].append((key, val))

    def lookup(self, look_key):
        idx = hash(look_key) % self.num
        for key, val in self.dictionary[idx]:
            if key == look_key:
                return val
        raise KeyError


if __name__ == "__main__":

    d = Dict()
    d.add("a", 0)
    d.add("b", 1)
    d.add("c", 2)

    print(d.lookup("b"))
    print(d.lookup("d"))
