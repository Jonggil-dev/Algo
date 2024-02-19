from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
conn=[[] for _ in range(N+1)]
basic=[[0]*(N+1) for _ in range(N+1)]
deg=[0]*(N+1)
for i in range(M):
    X,Y,K=map(int,input().split())
    conn[Y].append((X,K))
    deg[X]+=1

q=deque()
for i in range(1,N+1):
    if deg[i]==0:
        q.append(i)

while q:
    now=q.popleft()
    for next,next_basic in conn[now]:
        if basic[now].count(0)==N+1:
            basic[next][now]+=next_basic
        else:
            for i in range(1,N+1):
                basic[next][i]+=basic[now][i]*next_basic
        deg[next]-=1
        if deg[next]==0:
            q.append(next)
for x in enumerate(basic[N]):
    if x[1]>0:
        print(*x)