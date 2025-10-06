from collections import deque
import sys
input=sys.stdin.readline

def conv(x,y):
    return x%N,y%M


d=[0,0,1,-1]
N,M=map(int,input().split())
li=[list(map(int,input().split())) for i in range(N)]
visit=[[0]*(M) for _ in range(N)]
cnt=0

for x in range(N):
    for y in range(M):
        if visit[x][y] or li[x][y]:
            continue
        q=deque()
        q.append((x,y))
        cnt+=1
        visit[x][y]=cnt
        while q:
            nx,ny=q.popleft()
            for i in range(4):
                dx,dy=conv(nx+d[i],ny+d[3-i])
                if not visit[dx][dy] and li[dx][dy]==0:
                    q.append((dx,dy))
                    visit[dx][dy]=cnt
print(cnt)
