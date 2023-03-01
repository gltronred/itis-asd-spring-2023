#!/usr/bin/env python3

# 0 1 2 3 4 5 6 7 8
#
#         1
#   2           3
# 4   5       6   7
#8

import heapq as h

# создаём очередь с приоритетами (пустую)
heap = []

# вводим N чисел
n = int(input())
for _ in range(n):
    k = int(input())
    if k > 0:
        # если число > 0, вставляем в очередь
        h.heappush(heap, k)
    elif k < 0:
        # если < 0, вытаскиваем из очереди
        print(h.heappop(heap))
    else:
        # если == 0, выводим на экран всю очередь
        print(heap)
