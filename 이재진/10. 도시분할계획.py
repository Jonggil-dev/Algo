def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


import sys
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
edges.sort()
last = 0
result = 0
for e in edges:
    cost, a, b = e
    if find(a) != find(b):
        union(a, b)
        result += cost
        last = cost
print(result - last)