from collections import deque
import sys
input=sys.stdin.readline
d=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
N,M=map(int,input().split())
X,Y=map(int,input().split())
li=[[-1]*(N+1) for _ in range(N+1)]
li[X][Y]=0
q=deque()
q.append((X,Y))
while q:
    x,y=q.popleft()
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 1<=nx<=N and 1<=ny<=N:
            if li[nx][ny]==-1 or li[nx][ny]>li[x][y]+1:
                li[nx][ny]=li[x][y]+1
                q.append((nx,ny))
for i in range(M):
    A,B=map(int,input().split())
    print(li[A][B],end=" ")