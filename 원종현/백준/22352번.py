from collections import deque
N,M=map(int,input().split())
d=[0,0,1,-1]
before=[]
after=[]
for i in range(N):
    before.append(list(map(int,input().split())))
after=[]
for i in range(N):
    after.append(list(map(int,input().split())))
visit=[[0]*(M) for _ in range(N)]

r=0
f=0
for i in range(N):
    for j in range(M):
        if r>1:
            f=1
            break
        if not visit[i][j]:
            if after[i][j]!=before[i][j]:
                r+=1
            q=deque([])
            q.append((i,j))
            visit[i][j]=1
            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx=x+d[k]
                    ny=y+d[3-k]
                    if 0<=nx<N and 0<=ny<M and before[nx][ny]==before[x][y]:
                        if not visit[nx][ny] and after[nx][ny]==after[x][y]:
                            visit[nx][ny]=1
                            q.append((nx,ny))
                        if after[x][y]!=after[nx][ny]:
                            r+=1
                            break
    if f:
        break
print("YES" if r<=1 else "NO")