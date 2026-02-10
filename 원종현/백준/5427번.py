# pypy
from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]

for _ in range(int(input())):
    W,H=map(int,input().split())
    res='IMPOSSIBLE'
    st=[0,0]
    li=[]
    fire=deque([])
    visit=[[-1]*W for _ in range(H)]
    fires=[[-1]*W for _ in range(H)]
    for i in range(H):
        tmp=input().rstrip()
        for j in range(W):
            if tmp[j]=='@':
                st=[i,j]
            elif tmp[j]=='*':
                fire.append((i,j,0))
                fires[i][j]=0
        li.append(tmp)
    while fire:
        x,y,c=fire.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<H and 0<=ny<W and li[nx][ny]!='#' and (fires[nx][ny]==-1 or fires[nx][ny]>c+1):
                fire.append((nx,ny,c+1))
                fires[nx][ny]=c+1
    q=deque([(st[0],st[1],0)])
    visit[st[0]][st[1]]=0
    flag=0
    while q:
        x,y,c=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<H and 0<=ny<W:
                if li[nx][ny]!='#' and (visit[nx][ny]==-1 or visit[nx][ny]>c+1) and (fires[nx][ny]==-1 or fires[nx][ny]>c+1):
                    q.append((nx,ny,c+1))
                    visit[nx][ny]=c+1
            else:
                res=c+1
                flag=1
                break
        if flag:
            break
    print(res)