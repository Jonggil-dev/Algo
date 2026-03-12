from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]

W,H=map(int,input().split())
N=int(input())

li=[[0]*H for _ in range(W)]
visit=[[-1]*H for _ in range(W)]
q=deque()
count=0
for _ in range(N):
    a,x,y=input().rstrip().split()
    x,y=int(x),int(y)
    if a=='redstone_dust':
        li[x][y]=1
    elif a=='redstone_block':
        q.append((x,y,16))
        visit[x][y]=16
        li[x][y]=2
    else:
        li[x][y]=3
        count+=1


while q:
    x,y,c=q.popleft()
    if c==0:
        continue
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<W and 0<=ny<H and li[nx][ny]>0 and (visit[nx][ny]==-1 or visit[nx][ny]<c-1):
            if li[nx][ny]==3 and visit[nx][ny]==-1:
                visit[nx][ny]=c-1
                count-=1
            elif li[nx][ny]==1:
                visit[nx][ny]=c-1
                q.append((nx,ny,c-1))

print('success' if count==0 else 'failed')