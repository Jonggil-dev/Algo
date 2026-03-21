import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def func(now,dep):
    global res
    visit[now]=1
    if dep<=K:
        res+=li[now]
    for next in graph[now]:
        if not visit[next]:
            func(next,dep+1)


N,K=map(int,input().split())
graph=[[] for _ in range(N)]
visit=[0]*N
for i in range(N-1):
    p,c=map(int,input().split())
    graph[p].append(c)
li=list(map(int,input().split()))
res=0
func(0,0)
print(res)