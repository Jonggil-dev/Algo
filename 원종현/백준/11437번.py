import sys
sys.setrecursionlimit(int(1e5))
input=sys.stdin.readline

N=int(input())
nodes=[[0]*(20) for _ in range(N+1)]

depth=[0]*(N+1)
cal=[0]*(N+1)
graph=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,dep):
    cal[x]=1
    depth[x]=dep
    for y in graph[x]:
        if cal[y]:
            continue
        nodes[y][0]=x
        dfs(y,dep+1)

def lca(a,b):
    if depth[a]<depth[b]:
        a,b=b,a
    for j in range(19,-1,-1):
        if depth[a]-depth[b]>=2**j:
            a=nodes[a][j]
    if a==b:
        return a
    for j in range(19,-1,-1):
        if nodes[a][j]!= nodes[b][j]:
            a=nodes[a][j]
            b=nodes[b][j]
    return nodes[a][0]
dfs(1,0)
for i in range(1,20):
    for j in range(1,N+1):
        nodes[j][i]=nodes[nodes[j][i-1]][i-1]
M=int(input())
for i in range(M):
    a,b,=map(int,input().split())
    print(lca(a,b))
