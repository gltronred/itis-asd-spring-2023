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

    def print_list():
        # Write your code here!
        pass

def print_list(head: Elem):
    if head is None:
        print()
    else:
        print(head.val, " ")
        print_list(head.next)

# Более функциональный стиль

def empty_list() -> Elem:
    return None

def prepend(head: Elem, x: int) -> Elem:
    return Elem(x, head)

if __name__ == '__main__':
    head = List()
    head.prepend(3)
    head.prepend(4)
    head.prepend(5)

    print_list(Elem(5,Elem(4,Elem(3,None))))
