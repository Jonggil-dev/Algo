from collections import deque
import sys
input=sys.stdin.readline




N=int(input())
M=int(input())
graph=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit=[0]*(N+1)
res=0
q=deque()
q.append(1)
visit[1]=1
while q:
    now=q.popleft()
    for next in graph[now]:
        if visit[next]==0:
            q.append(next)
            visit[next]=visit[now]+1

for i in range(2,N+1):
    if 0<visit[i]<=3:
        res+=1
print(res)