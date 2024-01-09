from collections import deque
d={'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
N,M=map(int,input().split())
li=[input() for _ in range(N)]
visit=[[0]*(M) for _ in range(N)]
res=0

for i in range(N):
    for j in range(M):
        tmp={}
        q=deque([])
        if not visit[i][j]:
            tmp[(i,j)]=1
            q.append((i,j))
            while q:
                x,y=q.popleft()
                nx,ny=x+d[li[x][y]][0],y+d[li[x][y]][1]
                if 0<=nx<N and 0<=ny<M:
                    if (nx,ny) in tmp:
                        res+=1
                        break
                    elif visit[nx][ny]:
                        break
                    else:
                        tmp[(nx,ny)]=1
                        q.append((nx,ny))
                else:
                    res+=1
                    break
            for sx,sy in tmp.keys():
                visit[sx][sy]=1

print(res)