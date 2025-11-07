from collections import deque
import sys
input=sys.stdin.readline


N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[[]]+[[0]+list(map(int,input().split())) for _ in range(M)]

source,sink=0,N+M+1
graph=[[] for _ in range(N+M+2)]
capacity=[[0]*(N+M+2) for _ in range(N+M+2)]
cost=[[0]*(N+M+2) for _ in range(N+M+2)]
for i in range(N):
    graph[0].append(i+1)
    graph[i+1].append(0)
    capacity[0][i+1]=A[i]

for i in range(M):
    graph[1+N+i].append(1+N+M)
    graph[1+N+M].append(1+N+i)
    capacity[1+N+i][1+N+M]=B[i]

for i in range(N):
    for j in range(M):
        graph[i+1].append(N+j+1)
        graph[N+j+1].append(i+1)
        capacity[i+1][N+j+1]=1000
        cost[i+1][N+j+1]=C[j+1][i+1]
        cost[N+j+1][i+1]=-C[j+1][i+1]

tot_cost,tot_flow=0,0
flow=[[0]*(N+M+2) for _ in range(N+M+2)]
while True:
    dir=[-1]*(N+M+2)
    dist=[10**9]*(N+M+2)
    dist[0]=0
    q=deque([0])
    iq=[0]*(N+M+2)
    while q:
        now=q.popleft()
        iq[now]=0
        for next in graph[now]:
            if capacity[now][next]-flow[now][next]>0 and dist[next]>dist[now]+cost[now][next]:
                dist[next]=dist[now]+cost[now][next]
                dir[next]=now
                if not iq[next]:
                    q.append(next)
                    iq[next]=1
    if dir[sink]==-1:
        break
    tmp_flow=10**9
    b=sink
    while b!=source:
        a=dir[b]
        tmp_flow=min(tmp_flow,capacity[a][b]-flow[a][b])
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
