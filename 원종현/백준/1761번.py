import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(input())
depth=[0]*(N+1)
parent=[[0]*20 for _ in range(N+1)]
graph=[[] for _ in range(N+1)]
dist=[0]*(N+1)
for _ in range(N-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(x,par,val):
    for y,cost in graph[x]:
        if y==par:
            continue
        depth[y]=depth[x]+1
        dist[y]=val+cost
        parent[y][0]=x
        dfs(y,x,val+cost)
def lca(oa,ob):
    if depth[oa]<depth[ob]:
        oa,ob=ob,oa
    a,b=oa,ob
    for i in range(19,-1,-1):
        if depth[a]-depth[b]>=2**i:
            a=parent[a][i]
    if a==b:
        return dist[oa] + dist[ob] - 2 * dist[a]

    for i in range(19,-1,-1):
        if parent[a][i]!=parent[b][i]:
            a=parent[a][i]
            b=parent[b][i]
    return dist[oa]+dist[ob]-2*dist[parent[a][0]]
dfs(1,0,0)
for j in range(1,20):
    for i in range(1,N+1):
        parent[i][j]=parent[parent[i][j-1]][j-1]
M=int(input())
for i in range(M):
    a,b=map(int,input().split())
    print(lca(a,b))