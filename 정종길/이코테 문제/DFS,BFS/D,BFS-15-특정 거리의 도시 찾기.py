'''
설계
1. bfs로 최단거리 찾기
'''

from collections import deque

N,M,K,X = map(int,input().split())
Arr = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    Arr[s].append(e)

q = deque([X])
distance = [-1] * (N+1)
distance[X] = 0

while q:
    now = q.popleft()
    for next in Arr[now]:
        if distance[next] == -1:
            q.append(next)
            distance[next] = distance[now] + 1

cnt = 0
for i in range(len(distance)):
    if distance[i] == K:
        cnt = 1
        print(i)

if not cnt:
    print(-1)