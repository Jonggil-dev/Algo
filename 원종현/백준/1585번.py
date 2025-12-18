from collections import deque
import sys
input=sys.stdin.readline

INF=float('inf')
def func(cost):
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
    return tot_cost,tot_flow

N=int(input())
SIZE=N*2+2
source,sink=0,N*2+1
st=list(map(int,input().split()))
end=list(map(int,input().split()))
graph=[[] for _ in range(SIZE)]
capa=[[0]*SIZE for _ in range(SIZE)]
min_cost=[[0]*SIZE for _ in range(SIZE)]
max_cost=[[0]*SIZE for _ in range(SIZE)]
T=int(input())
F=int(input())

for i in range(1,N+1):
    graph[0].append(i)
    graph[i].append(0)
    graph[N+i].append(sink)
    graph[sink].append(N+i)
    capa[0][i]=1
    capa[N+i][sink]=1
    for j in range(N+1,N*2+1):
        if end[j-N-1]<=st[i-1]:
            continue
        capa[i][j]=1
        graph[i].append(j)
        graph[j].append(i)
        val=0 if end[j-N-1]-st[i-1]>T else min(F,(T-(end[j-N-1]-st[i-1]))**2)
        min_cost[i][j]=val
        min_cost[j][i]=-min_cost[i][j]
        max_cost[i][j]=-min_cost[i][j]
        max_cost[j][i]=min_cost[i][j]

min_res=func(min_cost)
max_res=func(max_cost)
if min_res[1]<N:
    print(-1)
else:
    print(min_res[0],-max_res[0])