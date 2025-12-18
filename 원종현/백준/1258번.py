from collections import deque
import sys
input=sys.stdin.readline
INF=float('inf')

N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
SIZE=N*2+2
graph=[[] for _ in range(SIZE)]
source,sink=0,N*2+1
capa=[[0]*SIZE for _ in range(SIZE)]
cost=[[0]*SIZE for _ in range(SIZE)]
for i in range(1,N+1):
    graph[0].append(i)
    graph[i].append(0)
    capa[0][i]=1
    for j in range(N+1,N*2+1):
        graph[i].append(j)
        graph[j].append(i)
        capa[i][j]=1
        cost[i][j]=li[i-1][j-1-N]
        cost[j][i]=-li[i-1][j-1-N]
for i in range(N+1,N*2+1):
    graph[i].append(sink)
    graph[sink].append(i)
    capa[i][sink]=1

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
print(tot_cost)