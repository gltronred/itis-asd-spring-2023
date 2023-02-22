#!/usr/bin/env python3

submits = list()

n = int(input())
for i in range(n):
    str = input().split()
    submits.append({'id': int(str[0]),
                    'prob': int(str[1]),
                    'time': int(str[2]),
                    'stat': str[3] == "C"})

participants = [[0 for p in range(10)]
                for id in range(101)]
penalty = [[0 for p in range(10)]
           for id in range(101)]
for submit in submits:
    id = submit['id']
    p = submit['prob']
    if submit['stat']:
        penalty[id][p] = penalty[id][p] + submit['time']
        participants[id][p] = 1
    else:
        penalty[id][p] = penalty[id][p] + 20

res = list()
for i in range(101):
    solved = sum(participants[i])
    pen = sum(penalty[i])
    if solved > 0:
        res.append((i, solved, pen))

# res.sort(...)
# sorted(...)

print(res)
