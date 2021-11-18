"""
Puzzle 07:

Implement a linked list class. A data type comprised of nodes,
where every node has 2 attributes: "value" of node (any type),
and "next" (pointer to next node).
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, init):
        self.head = Node(init)

    def __iter__(self):
        node = self.head
        yield node
        while node.next is not None:
            node = node.next
            yield node

    def __repr__(self):
        nodes = [str(node.data) for node in self]
        return " --> ".join(nodes)

    def append(self, val):
        for node in self:
            pass
        node.next = Node(val)

    def prepend(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def delete(self, val):
        for node in self:
            if node.next.data == val:
                break
        node.next = node.next.next

    def length(self):
        return sum(1 for node in self)


if __name__ == "__main__":

    link = LinkedList(1)
    print(link)

    link.append(4)
    link.append(3)
    link.prepend(5)
    print(link)

    link.delete(4)
    print(link)

    print(link.length())
