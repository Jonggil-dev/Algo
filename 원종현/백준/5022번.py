from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]

def bfs(st,end,visit):
    q=deque([[*st,0]])
    while q:
        x,y,c=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<=N and 0<=ny<=M and not visit[nx][ny]:
                q.append([nx,ny,c+1])
                visit[nx][ny]=[x,y]
                if [nx,ny]==end:
                    return c+1
    return -1
def func(a1,a2,b1,b2):
    res=0
    visit=[[0]*(M+1) for _ in range(N+1)]
    for x,y in [b1,b2]:
        visit[x][y]=1
    cost=bfs(a1,a2,visit)
    if cost==-1:
        return 1e5
    res+=cost
    dvisit=[[0]*(M+1) for _ in range(N+1)]
    x,y=a2
    while True:
        dvisit[x][y]=1
        if [x,y]==a1:
            break
        x,y=visit[x][y]
    cost=bfs(b1,b2,dvisit)
    if cost==-1:
        return 1e5
    res+=cost
    return res
N,M=map(int,input().split())
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
B1=list(map(int,input().split()))
B2=list(map(int,input().split()))

res1=func(A1,A2,B1,B2)
res2=func(B1,B2,A1,A2)
print("IMPOSSIBLE" if res1==1e5 and res2==1e5 else min(res1,res2))