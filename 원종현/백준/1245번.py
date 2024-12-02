from collections import deque
def check(x,y):
    return 0<=x<N and 0<=y<M
N,M=map(int,input().split())
d=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

li=[list(map(int,input().split())) for _ in range(N)]
visit=[[0]*(M) for _ in range(N)]
res=0
for i in range(N):
    for j in range(M): 
        if not visit[i][j]:
            bong=[(i,j)]
            q=deque()
            q.append((i,j))
            while q:
                x,y=q.popleft()
                for k in range(8):
                    nx,ny=x+d[k][0],y+d[k][1]
                    if check(nx,ny) and not visit[nx][ny] and (nx,ny) not in bong and li[x][y]==li[nx][ny]:
                        bong.append((nx,ny))
                        q.append((nx,ny))
            flag=1
            q=deque(bong)
            while q:
                x,y=q.popleft()
                for k in range(8):
                    nx,ny=x+d[k][0],y+d[k][1]
                    if check(nx,ny):
                        if visit[nx][ny] or([nx,ny] not in bong and li[x][y]<li[nx][ny]):
                            flag=0
                            break
                if not flag:
                    break
            if flag:
                res+=1
                for x,y in bong:
                    visit[x][y]=1
print(res)