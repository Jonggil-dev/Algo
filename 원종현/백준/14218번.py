from collections import deque
import sys
input=sys.stdin.readline

def func():
    q=deque()
    q.append((1,0))
    visit=[-1]*(N+1)
    visit[1]=0
    while q:
        now,c=q.popleft()
        for i in graph[now]:
            if visit[i]==-1 or visit[i]>c+1:
                visit[i]=c+1
                q.append((i,c+1))
    print(*visit[1:])

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    i,j=map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

Q=int(input())
for _ in range(Q):
    i,j=map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
    func()
