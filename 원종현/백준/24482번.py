import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def func(x):
    for i in graph[x]:
        if visit[i]==-1:
            visit[i]=visit[x]+1
            func(i)

N,M,R=map(int,input().split())
graph=[[]for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort(reverse=True)
visit=[-1]*(N+1)
visit[R]=0
func(R)

print(*visit[1:N+1],sep="\n")