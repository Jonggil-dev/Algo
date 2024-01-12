import sys,heapq
input=sys.stdin.readline

INF=int(1e15)
N,M,D,E=map(int,input().split())
h=[0]+list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
check={}
for i in range(M):
    a,b,n=map(int,input().split())
    a,b=min(a,b),max(a,b)
    if a==b:continue
    if (a,b) not in check or (check[(a,b)]>n):
        check[(a,b)]=n
for a,b in check.keys():
    graph[a].append((b,check[(a,b)]))
    graph[b].append((a,check[(a,b)]))
def dstra(st):
    q=[]
    distance=[INF]*(N+1)
    heapq.heappush(q,(st,0))
    distance[st]=0
    while q:
        now,dist=heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            if h[i[0]]<=h[now]:
                continue
            cost=i[1]+dist
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(i[0],cost))
    return distance
go=dstra(1)
back=dstra(N)
res=-INF
for i in range(2,N):
    if go[i]!=INF and back[i]!=INF:
        res=max(res,E*(h[i])-D*(go[i]+back[i]))
print(res if res!=-INF else 'Impossible')
