"""
Puzzle 08:

Implement a stack (last one in, first one out)
and a queue (first one in, first one out) data structure.

Methods: push, pop, length.
"""


class Stack:
    def __init__(self):
        self.stacked = []

    def push(self, val):
        self.stacked.append(val)

    def pop(self):
        self.stacked.pop()

    def length(self):
        return len(self.stacked)


class Queue:
    def __init__(self):
        self.queued = []

    def push(self, val):
        self.queued.append(val)

    def pop(self):
        self.queued.pop(0)

    def length(self):
        return len(self.queued)


if __name__ == "__main__":

    stacked = Stack()
    [stacked.push(i) for i in range(3)]

    stacked.pop()
    print(stacked.stacked)

    queued = Queue()
    [queued.push(i) for i in range(3)]

    queued.pop()
    print(queued.queued)
