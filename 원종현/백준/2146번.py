from collections import deque
d=[0,0,1,-1]
N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
res=10**9
visit=[[0]*(N) for _ in range(N)]
islands=[set()]
island_idx=0
for x in range(N):
    for y in range(N):
        if li[x][y]==1 and not visit[x][y]:
            q=deque()
            q.append((x,y))
            island_idx+=1
            islands.append({(x,y)})
            visit[x][y]=island_idx
            while q:
                x,y=q.popleft()
                for i in range(4):
                    nx,ny=x+d[i],y+d[3-i]
                    if 0<=nx<N and 0<=ny<N and li[nx][ny]==1 and not visit[nx][ny]:
                        visit[nx][ny]=island_idx
                        q.append((nx,ny))
                        islands[island_idx].add((nx,ny))

def func(idx):
    dist=[[-1]*(N) for _ in range(N)]
    q=deque()
    for x,y in islands[idx]:
        q.append((x,y))
        dist[x][y]=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 0<=nx<N and 0<=ny<N:
                if visit[nx][ny]!=0 and visit[nx][ny]!=idx:
                    return dist[x][y]
                elif visit[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
    return 10**9

def check(x,y):
    v=0
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<N and 0<=ny<N and li[nx][ny]==1:
            v+=1
    return 0 if v==4 else 1

for idx in range(1,len(islands)):
    now=func(idx)
    res=min(res,now)

print(res)
