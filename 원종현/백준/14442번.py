from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]
N,M,K=map(int,input().split())
li=[[*map(int,input().rstrip())] for _ in range(N)]

visit=[[11]*M for _ in range(N)]
visit[0][0]=0
q=deque([(0,0,1)])
res=-1
while q:
    x,y,c=q.popleft()
    if x==N-1 and y==M-1:
        res=c
        break
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<N and 0<=ny<M:
            v=visit[x][y]+li[nx][ny]
            if v<=K and v<visit[nx][ny]:
                visit[nx][ny]=v
                q.append((nx,ny,c+1))

print(res)