import sys
input=sys.stdin.readline

def getres(graph):
    for t in range(1,N+1):
        now=t
        dep=1
        while dep<=H:
            t+=graph[t][dep]
            dep+=1
        if now!=t:
            return 0
    return 1

def func(graph,c,x,y):
    global res
    if c>=res:
        return
    if getres(graph):
        res=min(res,c)
        return
    if c==3:
        return
    for i in range(x,N):
        st_y=y if i==x else 1
        for j in range(st_y,H+1):
            if graph[i][j]==0 and graph[i+1][j]==0:
                graph[i][j]=1
                graph[i+1][j]=-1
                func(graph,c+1,i+1 if j==H else i,1 if j==H else j+1)
                graph[i][j]=0
                graph[i+1][j]=0

N,M,H=map(int,input().split())
graph=[[0]*(H+2) for _ in range(N+1)]
res=4
for i in range(M):
    a,b=map(int,input().split())
    graph[b][a]=1
    graph[b+1][a]=-1

func(graph,0,1,1)
print(-1 if res>=4 else res)
