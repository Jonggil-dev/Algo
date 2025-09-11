from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]
N,M,K=map(int,input().split())

li=['.'*(M+1)]+['.'+input().rstrip() for _ in range(N)]
visit=[[-1]*(M+1) for _ in range(N+1)]
x1,y1,x2,y2=list(map(int,input().split()))
q=deque([])
q.append((x1,y1,0))
visit[x1][y1]=0

while q:
    x,y,c=q.popleft()
    for i in range(4):
        for j in range(1,K+1):
            nx,ny=x+d[i]*j,y+d[3-i]*j
            if 1<=nx<=N and 1<=ny<=M and li[nx][ny]=='.':
                if visit[nx][ny]==-1:
                    q.append((nx,ny,c+1))
                    visit[nx][ny]=c+1
                else:
                    if visit[nx][ny]<=c:
                        break
                    continue
            else:
                break
print(visit[x2][y2])
