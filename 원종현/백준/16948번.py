import sys
from collections import deque
sys.setrecursionlimit(10**6)
N=int(input())
r1,c1,r2,c2=map(int,input().split())
d=[(-2,-1),(-2,+1),(0,-2),(0,+2),(+2,-1),(+2,+1)]

visit=[[-1]*(N) for _ in range(N)]

q=deque()
q.append((r1,c1))
visit[r1][c1]=0
while q:
    x,y=q.popleft()
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        c=visit[x][y]
        if 0<=nx<N and 0<=ny<N and (visit[nx][ny]==-1 or c+1<visit[nx][ny]):
            visit[nx][ny]=c+1
            q.append((nx,ny))
print(visit[r2][c2] if visit[r2][c2]!=0 else -1)