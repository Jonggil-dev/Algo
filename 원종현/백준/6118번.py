from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

visit=[0]*(N+1)
q=deque()
q.append((1,0))
visit[1]=1
while q:
    now,v=q.popleft()
    for i in graph[now]:
        if visit[i]==0:
            q.append((i,v+1))
            visit[i]=visit[now]+1
print(visit.index(max(visit)),max(visit)-1,visit.count(max(visit)))