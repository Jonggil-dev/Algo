import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
visit=[-1]*(N+1)

def func(x,c):
    visit[x]=c
    for i in graph[x]:
        if visit[i]==-1:
            func(i,c+1)

for i in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

func(R,0)
print(*visit[1:],sep='\n')