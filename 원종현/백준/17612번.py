import sys,heapq
from collections import deque
input=sys.stdin.readline
N,k=map(int,input().split())

A,B=[],[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

q=[]
for i in range(k):
    heapq.heappush(q,(0,i))

time=[0]*k
res=[]
for i in range(N):
    t,x=heapq.heappop(q)
    time[x]+=B[i]
    heapq.heappush(q,(time[x],x))
    res.append((time[x],-x,i))

print(sum(A[t[2]]*(i+1) for i,t in enumerate(sorted(res))))