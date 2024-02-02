def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


import sys
v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v+1)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)
for i in range(1, v+1):
    parent[i] = find(i)
print(parent)