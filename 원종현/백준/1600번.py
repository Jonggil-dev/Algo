from collections import deque
import sys
d=[0,0,1,-1]
d2=[2,2,-2,-2,1,-1,1,-1]
inf=float('inf')
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
K=int(input())
W,H=map(int,input().split())
li=[]
res=10**9
for i in range(H):
    li.append(list(map(int,input().split())))

q=deque([])
q.append((0,0,0,0))
visit=[[[inf]*(W) for _ in range(H)] for _ in range(K+1)]
for i in range(K+1):
    visit[i][0][0]=0
while q:
    x,y,c,t=q.popleft()
    for i in [1,2]:
        if i==1:
            for j in range(4):
                nx,ny=x+d[j],y+d[3-j]
                if 0<=nx<H and 0<=ny<W and visit[c][nx][ny]>t+1 and not li[nx][ny]:
                    visit[c][nx][ny]=t+1
                    q.append((nx,ny,c,t+1))
        else:
            for j in range(8):
                nx,ny=x+d2[j],y+d2[7-j]
                if 0<=nx<H and 0<=ny<W and c<K and visit[c+1][nx][ny]>t+1 and not li[nx][ny]:
                    visit[c+1][nx][ny]=t+1
                    q.append((nx,ny,c+1,t+1))

res=inf
for i in range(K+1):
    res=min(res,visit[i][H-1][W-1])
print(res if res!=inf else -1)