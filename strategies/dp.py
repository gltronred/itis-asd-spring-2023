"""
5
w c
4 4  <- greedy
2 3
2 3
1 1
"""

class Item:
    def __init__(self, w, c):
        self.weight = w
        self.cost = c

w = int(input())
m = int(input())
c = list()
for i in range(m):
    s = input().split()
    weight = int(s[0])
    cost = int(s[1])
    c.append(Item(weight, cost))

"""
f(0,k) = 0
f(n,0) = 0 if n < w_0, f(n,0) = c_0 if n >= w_0
f(n,k) = max { f(n-w_k, k-1) + c_k, f(n, k-1) }
"""

a = [[0 for n in range(w+1)] for k in range(m)]
b = [[0 for n in range(w+1)] for k in range(m)]
for n in range(c[0].weight, w+1):
    a[0][n] = c[0].cost
    b[0][n] = 1

for k in range(1, m):
    for n in range(w+1):
        max = a[k-1][n]
        imax = 0
        if n - c[k].weight >= 0:  # можно ли взять k-й предмет
            # нужно ли брать k-й предмет (даст ли это большую сумму)
            if max < a[k-1][n - c[k].weight] + c[k].cost:
                max = a[k-1][n - c[k].weight] + c[k].cost
                imax = 1
        a[k][n] = max
        b[k][n] = imax

print("a")
for k in range(m):
    print(a[k])
print("b")
for k in range(m):
    print(b[k])

print(a[m-1][w])

r = m * [0]
n = w
for k in range(m-1, -1, -1):
    r[k] = b[k][n]
    if b[k][n] == 1:
        n -= c[k].weight
print(r)
