"""
Puzzle 09:

Implement a binary tree class.

Methods: insert, contains and map.
"""


class BinaryTree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

    def insert(self, val):
        if self.node > val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinaryTree(val)

        elif self.node < val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinaryTree(val)

    def contains(self, val):
        if self.node == val:
            return True
        if self.left == None and self.right == None:
            return False

        if self.node > val:
            if self.left:
                return self.left.contains(val)

        elif self.node < val:
            if self.right:
                return self.right.contains(val)

    def map(self, func):
        self.node = func(self.node)
        if self.left:
            self.left.map(func)

        if self.right:
            self.right.map(func)


if __name__ == "__main__":

    bt = BinaryTree(10)

    bt.insert(2)
    bt.insert(11)
    print(bt.contains(11))

    bt.map(lambda x: x ** 2)
    print(bt.contains(121))
