import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**4)
N,M,K=map(int,input().split())
price=[0]+list(map(int,input().split()))

def func(x,idx):
    global price,visit
    for i in graph[x]:
        if not visit[i]:
            visit[i]=idx
            group_min_price[idx]=min(group_min_price[idx],price[i])
            func(i,idx)

graph=[set() for _ in range(N+1)]
visit=[0]*(N+1)
group_min_price={}
for _ in range(M):
    v,w=map(int,input().split())
    graph[v].add(w)
    graph[w].add(v)

idx=1
for i in range(1,N+1):
    if not visit[i]:
        visit[i]=idx
        group_min_price[idx]=price[i]
        func(i,idx)
        idx+=1
res=sum([i for i in group_min_price.values()])
print(res if res<=K else "Oh no")