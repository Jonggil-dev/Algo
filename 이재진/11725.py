import sys
from collections import deque
N = int(sys.stdin.readline())
dic = {i:[] for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
q = deque()
visited = [0]*(N+1)
visited[1] = 1
ls = [0]*(N+1)
q.append(1)
while q:
    x = q.popleft()
    for i in dic[x]:
        if not visited[i]:
            ls[i] = x
            visited[i] = 1
            q.append(i)
for i in ls[2:]:
    print(i)