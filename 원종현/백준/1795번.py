from collections import deque
d=[[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
N,M=map(int,input().split())
li=[]
horse=[]
for i in range(N):
    tmp=input()
    for j in range(M):
        if tmp[j]!='.':
            horse.append((i,j,int(tmp[j])))

check1=[[0]*(M) for i in range(N)]
check2=[[0]*(M) for i in range(N)]

def func(sx,sy,k):
    global check1,check2
    q=deque()
    visit=[[0]*(M) for i in range(N)]
    visit[sx][sy]=1
    check2[sx][sy]+=1
    q.append((sx,sy,k,1))
    while q:
        x,y,c,g=q.popleft()
        if c==0:
            c=k
            g+=1
        for dx,dy in d:
            nx=x+dx
            ny=y+dy
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
                q.append((nx,ny,c-1,g))
                check2[nx][ny]+=1
                visit[nx][ny]=1
                check1[nx][ny]+=g

for kx,ky,kc in horse:
    func(kx,ky,kc)
r=10**9
for i in range(N):
    for j in range(M):
        if check2[i][j]==len(horse):
            r=min(r,check1[i][j])
if len(horse)==1:
    print(0)
else:
    print(r if r!=10**9 else -1)