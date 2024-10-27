import heapq
N=int(input())
T,M=map(int,input().split())
L=int(input())
INF=10**9
graph=[[] for _ in range(N+1)]
for i in range(L):
    a,b,t,m=map(int,input().split())
    graph[a].append((b,m,t))
    graph[b].append((a,m,t))

q=[]
distance=[[INF]*(M+1) for _ in range(N+1)]
heapq.heappush(q,(1,0,0))
distance[1][0]=0
while q:
    now,t,m=heapq.heappop(q)
    if distance[now][m]<t:
        continue
    for next,money,time in graph[now]:
        if time+t>T or money+m>M:
            continue
        if time+t<distance[next][money+m]:
            distance[next][money+m]=time+t
            heapq.heappush(q,(next,time+t,money+m))

res=-1
for i in range(M+1):
    if distance[N][i]<=T:
        res=i
        break
print(res)
