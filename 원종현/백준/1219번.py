from collections import deque
INF=float('inf')
N,S,E,M=map(int,input().split())
graph=[[] for _ in range(N)]
dist=[-INF]*(N)
tmp=[]

for _ in range(M):
    a,b,c=map(int,input().split())
    tmp.append((a,b,c))
cost=list(map(int,input().split()))
visit=[0]*(N)

for a,b,c in tmp:
    graph[a].append((b,cost[b]-c))

def func(s):
    dist[s]=cost[S]
    for i in range(N):
        for j in range(N):
            for b,c in graph[j]:
                if dist[j]!=-INF and dist[b]<dist[j]+c:
                    visit[b]=1
                    dist[b]=dist[j]+c
                    if i==N-1:
                        dist[b]=INF

def check(i):
    q=deque()
    q.append(i)
    visit=[0]*(N)
    visit[i]=1
    while q:
        now=q.popleft()
        if now==E:
            return 1
        for next,_ in graph[now]:
            if not visit[next]:
                visit[next]=1
                q.append(next)
    return 0

func(S)
plag=0
for i in range(N):
    if dist[i]==INF:
        if check(i):
            plag=1
            break

if plag:
    print('Gee')
elif S!=E and visit[E]==0:
    print('gg')
else:
    print(dist[E])
print(plag)
print(dist)
print(visit)
print(graph)