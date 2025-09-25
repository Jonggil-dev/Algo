from collections import deque
N,M=map(int,input().split())
graph=[set() for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

def func():
    visit=[-1]*(N+1)
    visit[1]=1
    q=deque()
    q.append((1,0))
    while q:
        x,c=q.popleft()
        for i in graph[x]:
            if visit[i]==-1 or visit[i]>c+1:
                visit[i]=c+1
                q.append((i,c+1))
    visit[1]=0
    return visit[1:]
Q=int(input())
res=[0]*(Q)
for _ in range(Q):
    a,i,j=map(int,input().split())
    if a==1:
        graph[i].add(j)
        graph[j].add(i)
    else:
        graph[i].remove(j)
        graph[j].remove(i)
    print(*func())
