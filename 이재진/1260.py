def dfs(x, v):
    v[x] = 1
    print(x, end=' ')
    for w in sorted(dic[x]):
        if not v[w]:
            dfs(w, v)


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    res = []
    while q:
        v = q.popleft()
        res.append(v)
        for w in sorted(dic[v]):
            if not visited[w]:
                visited[w] = 1
                q.append(w)
    return res


import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
dic = {i: [] for i in range(1, 1001)}
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    dic[x].append(y)
    dic[y].append(x)
visited = [0] * 1001
dfs(V, visited)
print()
visited = [0] * 1001
res_b = bfs(V)
print(*res_b)