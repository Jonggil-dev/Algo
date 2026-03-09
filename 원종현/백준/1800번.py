import sys,heapq
input=sys.stdin.readline

N,P,K=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(P):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def check(val):
    dist=[float('inf')]*(N+1)
    dist[1]=0
    q=[(0,1)]
    while q:
        c,now=heapq.heappop(q)
        if dist[now]<c:
            continue
        for next,v in graph[now]:
            cost=(1 if v>val else 0)+c
            if dist[next]>cost:
                dist[next]=cost
                heapq.heappush(q,(cost,next))
    return dist[N]<=K

res=-1
le,ri=0,1000000
while le<=ri:
    mid=(le+ri)//2
    if check(mid):
        res=mid
        ri=mid-1
    else:
        le=mid+1
print(res)