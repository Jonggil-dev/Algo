from collections import deque
import sys
input=sys.stdin.readline


N,P=map(int,input().split())
capa=[[0]*(N*2) for _ in range(N*2)]
flow=[[0]*(N*2) for _ in range(N*2)]
graph=[[] for _ in range(N*2)]
for i in range(N):
    graph[i].append(i+N)
    graph[i+N].append(i)
    capa[i][i+N]=1

for _ in range(P):
    a,b=map(lambda x:int(x)-1,input().split())
    capa[a+N][b]=1
    capa[b+N][a]=1
    graph[a].append(b+N)
    graph[a+N].append(b)
    graph[b].append(a+N)
    graph[b+N].append(a)

st,end=N,1
res=0
while True:
    visit=[-1]*(N*2)
    q=deque()
    q.append(st)
    while q:
        now=q.popleft()
        for next in graph[now]:
            if capa[now][next]-flow[now][next]>0 and visit[next]==-1:
                q.append(next)
                visit[next]=now
    if visit[end]==-1:
        break
    now=end
    while now!=st:
        flow[visit[now]][now]+=1
        flow[now][visit[now]]-=1
        now=visit[now]
    res+=1

print(res)