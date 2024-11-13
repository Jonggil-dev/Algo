from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
ind=[0]*(N+1)
graph=[[] for _ in range(N+1)]
for i in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    ind[B]+=1

res=[1]*(N+1)
q=deque()
for i in range(1,N+1):
    if not ind[i]:
        q.append(i)
while q:
    now=q.popleft()
    for i in graph[now]:
        ind[i]-=1
        if not ind[i]:
            q.append(i)
        res[i]=res[now]+1
print(*res[1:])