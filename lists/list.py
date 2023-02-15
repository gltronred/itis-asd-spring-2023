#!/usr/bin/env python3

#
# 5 -> 4 -> 3 -> None
#

class Elem:
    def __init__(self, x, p):
        self.val = x
        self.next = p

# Объектно-ориентированный стиль

class List:
    def __init__(self):
        self.head = None
    def prepend(self, x: int):
        self.head = Elem(x, self.head)
    def print_list(self):
        p = self.head
        while p is not None:
            print(p.val)
            p = p.next

    def length(self) -> int:
        # Write a function to compute length of the list
        pass

if __name__ == '__main__':
    head = List()
    head.prepend(3)
    head.prepend(4)
    head.prepend(5)
    head.print_list()
