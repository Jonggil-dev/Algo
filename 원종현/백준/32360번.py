from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]
N,M=map(int,input().split())
K,C=map(int,input().split())
li=[]
st,end=[0,0],[0,0]
for i in range(N):
    tmp=input().rstrip()
    li.append(tmp)
    for j in range(M):
        if tmp[j]=='S':
            st=[i,j]
        elif tmp[j]=='E':
            end=[i,j]

visit=[[[float('inf')]*100 for _ in range(M)] for i in range(N)]

q=deque()
q.append((st[0],st[1],0,0))
visit[st[0]][st[1]][0]=0
while q:
    x,y,c,t=q.popleft()
    if li[x][y]=='H' and visit[x][y][max(0,c-K)]>t+1:
        visit[x][y][max(0,c-K)]=t+1
        q.append((x,y,max(0,c-K),t+1))
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<N and 0<=ny<M and li[nx][ny]!='#':
            if li[nx][ny] in 'E.':
                nc=c+C
            else:
                nc=max(0,c-K)
            if nc<100 and visit[nx][ny][nc]>t+1:
                visit[nx][ny][nc]=t+1
                if [nx,ny]!=end:
                    q.append((nx,ny,nc,t+1))
res=min(visit[end[0]][end[1]])
print(res if res!=float('inf') else -1)
