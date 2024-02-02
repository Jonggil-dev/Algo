def find(x):
    if head[x] != x:
        find(head[x])
    return x


def union(a, b):
    A = find(a)
    B = find(b)
    if A > B:
        head[a] = b
    else:
        head[b] = a


import sys
n, m = map(int, sys.stdin.readline().split())
head = [i for i in range(n+1)]
for _ in range(m):
    x, a, b = map(int, sys.stdin.readline().split())
    if x == 0:
        union(a, b)
    elif x == 1:
        A = find(a)
        B = find(b)
        if A == B:
            print("YES")
        else:
            print("NO")