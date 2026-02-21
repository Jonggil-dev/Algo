from collections import deque
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visit=[-1]*(N+1)
q=deque()
q.append((a,0))
visit[a]=0

while q:
    now,c=q.popleft()
    for i in graph[now]:
        if visit[i]==-1 or visit[i]>c+1:
            q.append((i,c+1))
            visit[i]=c+1

print(visit[b] if visit[b]<=M else -1)