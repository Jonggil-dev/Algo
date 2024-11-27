import heapq
import sys
input=sys.stdin.readline
INF=float(1e9)
N,M=map(int,input().split())
graph=[[float(1e9)]*(N+1) for _ in range(N+1)]
graph_max=[[0]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    graph[i][i]=0

for i in range(M):
    S,E,L=map(int,input().split())
    graph[S][E]=min(graph[S][E],L)
    graph[E][S]=min(graph[E][S],L)
    graph_max[S][E]=max(graph_max[S][E],L)
    graph_max[E][S]=max(graph_max[E][S],L)


for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

res=10**9
for node in range(1,N+1):
    tmp_res=0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if not graph_max[i][j]:
                continue
            a,b=graph[node][i],graph[node][j]
            if a>b:a,b=b,a
            tmp=graph_max[i][j]-(b-a)
            tmp_res=max(tmp_res,b+tmp/2)
    res=min(res,tmp_res)
print(res)
