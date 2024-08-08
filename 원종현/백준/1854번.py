import sys,heapq
input=sys.stdin.readline

INF=float('inf')
N,M,K=map(int,input().split())
graph=[[] for _ in range(N+1)]
distance=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

q=[]
heapq.heappush(distance[1],0)
heapq.heappush(q,(0,1))

while q:
    dist,now=heapq.heappop(q)
    for i in graph[now]:
        cost=dist+i[1]
        if len(distance[i[0]])<K:
            heapq.heappush(distance[i[0]],-cost)
            heapq.heappush(q,(cost,i[0]))
        elif cost<-distance[i[0]][0]:
            heapq.heappop(distance[i[0]])
            heapq.heappush(distance[i[0]],-cost)
            heapq.heappush(q,(cost,i[0]))

for i in range(1,N+1):
    if len(distance[i])==K:
        print(-distance[i][0])
    else:
        print(-1)