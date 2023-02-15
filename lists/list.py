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
        n = 0
        p = self.head
        while p is not None:
            n = n+1
            p = p.next
        return n

# Из списка orig скопировать чётные элементы в новый список
# Исходный список остаётся без изменений
def only_even(orig: List) -> List:
    return orig

if __name__ == '__main__':
    head = List()
    head.prepend(3)
    head.prepend(4)
    head.prepend(6)
    head.prepend(5)
    head.print_list()

    print('Length')
    print(head.length())

    print('Only even')
    evens = only_even(head)
    print('Orig')
    head.print_list()           # 5,6,4,3
    print('Evens')
    evens.print_list()          # 6,4
