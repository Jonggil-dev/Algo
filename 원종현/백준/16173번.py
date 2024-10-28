from collections import deque
N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
d=[1,0]
visit=[[0]*3 for _ in range(N)]
q=deque()
q.append((0,0))
while q:
    x,y=q.popleft()
    for i in range(2):
        nx,ny=x+d[i]*li[x][y],y+d[1-i]*li[x][y]
        if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
            visit[nx][ny]=1
            q.append((nx,ny))
print("HaruHaru" if visit[N-1][N-1] else "Hing")