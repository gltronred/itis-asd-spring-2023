#!/usr/bin/env python3


def gen(n):
    """Collatz conjecture."""
    i = n
    while i > 1:
        yield i
        if i % 2 == 0:
            i = int(i/2)
        else:
            i = 3 * i + 1


# for x in gen(11):
#     print(x)


def gen2(n):
    i = n
    while i > 0:
        yield i
        i = i + 1


for x in gen2(1):
    print(x)
    if x > 5:
        break
