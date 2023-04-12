#!/usr/bin/env python3


import itertools


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

# [1,2,...,9]
#   [2,...,9]
#
# S is subset [2,...,9] =>        S  is subset [1,2,...,9]
#                       => ([1] + S) is subset [1,2,...,9]
#
# S is subset [1,2,...,9] => either S is subset [2,...,9]
#                            or S \ [1] is subset [2,...,9]


# for i in powerset([1, 2, 3]):
#     print(i)


# 1,2,3,4,5
# 3,2,4,1,5

# 1,2,3,4,5
# 1,2,3,5,4
# 1,2,4,3,5
# ...
# 5,4,3,2,1

# 1,3,2,5,4
#       ^ ^
#       i
#     2,5,4
# 1,3,4,2,5
# 1,3,4,5,2
#       ^ ^
#       i
# 1,3,5,2,4

# 1,3,5,4,2
# 1,4,2,3,5
#
# a_1...a_{i-2} a_{i-1} < a_i > a_{i+1} >...a_{m-1} >   a_m   > a_{m+1}...> a_n
# a_1...a_{i-2}   a_m     a_n < a_{n-1} <...a_{m+1} < a_{i-1} < a_{m-1}...< a_i

def permutations(n):
    """Return permutations of [1,2,...,n]."""
    # First permutation
    p = [i+1 for i in range(n)]

    flag = True
    while flag:
        yield p

        # What part of permutation should we change?
        i = len(p) - 1
        while i > 0 and p[i-1] > p[i]:
            i -= 1

        # If all permutation is in reverse order, then we finish
        flag = i > 0
        # Otherwise, we change a part:
        if flag:
            # p[i-1] < p[i]
            # Find m: p[m] - minimal element greater than p[i-1]
            m = i
            for j in range(i+1, n):
                if p[j] < p[m] and p[j] > p[i-1]:
                    m = j
            # Swap p[m] and p[i-1]
            t = p[m]
            p[m] = p[i-1]
            p[i-1] = t
            # Sort p[i:] - same as reverse p[i:] here
            p[i:] = reversed(p[i:])


for p in permutations(4):
    print(p)
