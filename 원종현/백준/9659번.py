import sys,heapq
from collections import deque
input=sys.stdin.readline
def dstra():
    q=[]
    distance[S]=0
    heapq.heappush(q,(0,S))
    while q:
        dist,now=heapq.heappop(q)
        if now==D:
            return
        for v in graph[now]:
            cost=dist+graph[now][v]
            if cost<distance[v]:
                distance[v]=cost
                heapq.heappush(q,(cost,v))

def bfs():
    q=deque()
    q.append(D)
    while q:
        now=q.popleft()
        if now==S:
            continue
        for before,price in r_graph[now]:
            if distance[before]+graph[before][now]==distance[now]:
                if (before,now) not in tmp:
                    tmp.add((before,now))
                    q.append(before)

INF=1e9
while True:
    N,M=map(int,input().split())
    if N==0 and M==0:break
    S,D=map(int,input().split())
    graph=[{} for _ in range(N)]
    r_graph=[[] for _ in range(N)]
    tmp=set()
    for _ in range(M):
        U,V,P=map(int,input().split())
        graph[U][V]=P
        r_graph[V].append((U,P))
    distance=[INF]*N
    dstra()
    if distance[D]==INF:
        print(-1)
        continue
    bfs()
    for a,b in tmp:
        del graph[a][b]
    distance=[INF]*N
    dstra()
    print(distance[D] if distance[D]!=INF else -1)
