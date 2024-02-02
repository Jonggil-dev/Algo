import sys
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)
for i in range(1, N+1):
    find(i)
res = len(set(parent)) - 1
print(res)
