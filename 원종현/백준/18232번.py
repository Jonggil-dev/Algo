from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
S,E=map(int,input().split())
graph=[set() for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    graph[x].add(y)
    graph[y].add(x)
for i in range(1,N+1):
    if i==1:
        graph[i].add(i+1)
    elif i==N:
        graph[i].add(i-1)
    else:
        graph[i].add(i-1)
        graph[i].add(i+1)

visit=[-1]*(N+1)
visit[S]=0
q=deque()
q.append((S,0))
while q:
    x,c=q.popleft()
    for i in graph[x]:
        if visit[i]==-1 or c+1<visit[i]:
            visit[i]=c+1
            q.append((i,c+1))
print(visit[E])