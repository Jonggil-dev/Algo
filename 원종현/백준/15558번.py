import sys
from collections import deque
input=sys.stdin.readline
N,K=map(int,input().split())
d=[1,-1,K]
def func():
    q=deque()
    q.append((0,0,0))
    while q:
        idx,dir,t=q.popleft()
        for i in range(3):
            next=idx+d[i]
            if next>=N:
                return 1
            if next<=t:
                continue
            if arr[dir][next]==1 and i!=2 and visit[dir][next]==0:
                q.append((next,dir,t+1))
                visit[dir][next]=1
            elif i==2 and arr[1-dir][next]==1 and visit[1-dir][next]==0:
                q.append((next,1-dir,t+1))
                visit[1-dir][next]=1
    return 0

le=list(map(int,input().rstrip()))
ri=list(map(int,input().rstrip()))

visit=[[0]*(N) for _ in range(2)]
arr=[le,ri]
visit[0][0]=1

print(func())