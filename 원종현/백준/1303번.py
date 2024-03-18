from collections import deque
M,N=map(int,input().split())
a,b=0,0
d=[0,0,1,-1]
li=[input() for _ in range(N)]
visit=[[0]*(M) for _ in range(N)]
for x in range(N):
    for y in range(M):
        if not visit[x][y]:
            now=1

            q=deque([])
            q.append((x,y))
            visit[x][y]=1
            while q:
                sx,sy=q.popleft()
                for i in range(4):
                    nx=sx+d[i]
                    ny=sy+d[3-i]
                    if 0<=nx<N and 0<=ny<M and not visit[nx][ny] and li[x][y]==li[nx][ny]:
                        now+=1
                        visit[nx][ny]=1
                        q.append((nx,ny))
            if li[x][y]=='W':
                a+=now**2
            else:
                b+=now**2

print(a,b)