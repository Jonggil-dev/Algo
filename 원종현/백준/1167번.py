from collections import deque

V=int(input())
graph=[[]for _ in range(V+1)]
def bfs(st):
    visit=[-1]*(V+1)
    visit[st]=0
    q=deque()
    q.append((st,0))
    while q:
        now,dist=q.popleft()
        for a,b in graph[now]:
            if not visit[a]:
                cost=b+dist
                visit[a]=cost
                q.append((a,cost))
    r=max(visit)
    return [visit.index(r),r]

for i in range(V):
    tmp=list(map(int,input().split()))
    for j in range(1,len(tmp)-2,2):
        graph[tmp[0]].append((tmp[j],tmp[j+1]))
u=bfs(1)
v=bfs(u[0])
print(v[1])