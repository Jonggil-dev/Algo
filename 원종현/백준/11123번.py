from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]
for _ in range(int(input())):
    H,W=map(int,input().split())
    li=[input().rstrip() for _ in range(H)]
    visit=[[0]*W for _ in range(H)]
    res=0
    for x in range(H):
        for y in range(W):
            if not visit[x][y] and li[x][y]!='.':
                visit[x][y]=1
                q=deque([(x,y)])
                res+=1
                while q:
                    nx,ny=q.popleft()
                    for i in range(4):
                        dx,dy=nx+d[i],ny+d[3-i]
                        if 0<=dx<H and 0<=dy<W and not visit[dx][dy] and li[dx][dy]!='.':
                            q.append((dx,dy))
                            visit[dx][dy]=1
            else:
                continue
    print(res)