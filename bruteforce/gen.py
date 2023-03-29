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


def powerset(set):
    """Return all subsets of set."""
    if len(set) == 0:
        yield []
    else:
        r = set[0]
        for j in powerset(set[1:]):
            yield j
            yield [r] + j


for i in powerset([1, 2, 3]):
    print(i)
