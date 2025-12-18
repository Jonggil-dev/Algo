from collections import deque
import sys
input=sys.stdin.readline
INF=float('inf')


def func():
    tot_cost,tot_flow=0,0
    flow=[[0]*SIZE for _ in range(SIZE)]
    while True:
        dir=[-1]*SIZE
        dist=[INF]*SIZE
        dist[0]=0
        q=deque([0])
        iq=[0]*SIZE
        while q:
            now=q.popleft()
            iq[now]=0
            for next in graph[now]:
                if capa[now][next]-flow[now][next]>0 and dist[next]>dist[now]+cost[now][next]:
                    dist[next]=dist[now]+cost[now][next]
                    dir[next]=now
                    if not iq[next]:
                        q.append(next)
                        iq[next]=1
        if dir[sink]==-1:
            break
        tmp_flow=INF
        b=sink
        while b!=source:
            a=dir[b]
            tmp_flow=min(tmp_flow,capa[a][b]-flow[a][b])
            b=a
        b=sink
        while b!=source:
            a=dir[b]
            flow[a][b]+=tmp_flow
            flow[b][a]-=tmp_flow
            tot_cost+=cost[a][b]*tmp_flow
            b=a
        tot_flow+=tmp_flow
    return sum(flow[source]),tot_cost
N,M=map(int,input().split())
SIZE=N+M+2
source,sink=0,N+M+1
graph=[[] for _ in range(SIZE)]
capa=[[0]*SIZE for _ in range(SIZE)]
cost=[[0]*SIZE for _ in range(SIZE)]

for i in range(1,N+1):
    graph[0].append(i)
    graph[i].append(0)
    capa[0][i]=1
for i in range(N+1,N+M+1):
    graph[i].append(sink)
    graph[sink].append(i)
    capa[i][sink]=1
for i in range(1,N+1):
    n,*tmp=map(int,input().split())
    for j in range(0,n*2,2):
        x,y=tmp[j],tmp[j+1]
        cost[i][N+x]=y
        cost[N+x][i]=-y
        capa[i][N+x]=1
        graph[i].append(N+x)
        graph[N+x].append(i)

print(*func())