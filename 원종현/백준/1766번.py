import sys,heapq
input=sys.stdin.readline
N,M=map(int,input().split())
C=[0]*(N+1)
graph=[[] for _ in range(N+1)]
q=[]
for i in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    C[B]+=1
for i in range(1,N+1):
    if C[i]==0:
        heapq.heappush(q,i)

while q:
    now=heapq.heappop(q)
    print(now,end=' ')
    for i in graph[now]:
        C[i]-=1
        if C[i]==0:
            heapq.heappush(q,i)