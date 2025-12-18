from collections import deque
import sys
input=sys.stdin.readline
INF=float('inf')

for idx in range(int(input())):
    N,a,b,c,d,e,f=map(int,input().split())
    A,B=[a,b,c],[d,e,f]
    li=[list(map(int,input().split())) for _ in range(3)]
    graph=[[] for _ in range(8)]
    source,sink=0,7
    capa=[[0]*(8) for _ in range(8)]
    cost=[[0]*(8) for _ in range(8)]

    for i in range(1,4):
        graph[0].append(i)
        graph[i].append(0)
        capa[0][i]=A[i-1]
        for j in range(1,4):
            graph[i].append(3+j)
            graph[3+j].append(i)
            cost[i][3+j]=-li[i-1][j-1]
            cost[3+j][i]=li[i-1][j-1]
            capa[i][3+j]=N
    for i in range(1,4):
        graph[3+i].append(7)
        graph[7].append(3+i)
        capa[3+i][7]=B[i-1]

    tot_cost,tot_flow=0,0
    flow=[[0]*(8) for _ in range(8)]
    while True:
        dir=[-1]*(8)
        dist=[INF]*(8)
        dist[0]=0
        q=deque([0])
        iq=[0]*(8)
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
    print(f'Case #{idx+1}: {-tot_cost}')