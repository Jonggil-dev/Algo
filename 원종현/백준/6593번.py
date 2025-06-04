from collections import deque
import sys
input=sys.stdin.readline
d=[(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
while True:
    L,R,C=map(int,input().split())
    if L==0 and R==0 and C==0:
        break
    li=[]
    st,end=[0,0,0],[0,0,0]
    for i in range(L):
        tmp=[]
        for j in range(R):
            now=input().rstrip()
            for k in range(C):
                if now[k]=='S':
                    st=[i,j,k]
                elif now[k]=='E':
                    end=[i,j,k]
            tmp.append(now)
        li.append(tmp)
        input()
    visit=[[[-1]*C for _ in range(R)] for _ in range(L)]

    q=deque()
    q.append(st)
    visit[st[0]][st[1]][st[2]]=0
    while q:
        x,y,z=q.popleft()
        if [x,y,z]==end:
            break
        for dx,dy,dz in d:
            nx,ny,nz=x+dx,y+dy,z+dz
            if 0<=nx<L and 0<=ny<R and 0<=nz<C:
                if li[nx][ny][nz]!='#' and visit[nx][ny][nz]==-1:
                    visit[nx][ny][nz]=visit[x][y][z]+1
                    q.append((nx,ny,nz))

    if visit[end[0]][end[1]][end[2]]!=-1:
        print(f'Escaped in {visit[end[0]][end[1]][end[2]]} minute(s).')
    else:
        print('Trapped!')
