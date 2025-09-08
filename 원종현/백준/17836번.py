from collections import deque
N,M,T=map(int,input().split())
d=[0,0,1,-1]
li=[]
g=[0,0]
for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(M):
        if tmp[j]==2:
            g=[i,j]
    li.append(tmp)

visit=[[-1]*(M) for _ in range(N)]
visit[0][0]=0
q=deque([])
q.append((0,0,0))
while q:
    x,y,t=q.popleft()
    for i in range(4):
        nx,ny=x+d[i],y+d[3-i]
        if 0<=nx<N and 0<=ny<M and li[nx][ny]!=1 and t<T  and (visit[nx][ny]==-1 or visit[nx][ny]>t+1):
            visit[nx][ny]=t+1
            q.append((nx,ny,t+1))
g_v=abs(g[1]-(M-1))+abs(g[0]-(N-1))
res=-1
if visit[N-1][M-1]!=-1 and visit[g[0]][g[1]]!=-1:
    res=min(visit[N-1][M-1],visit[g[0]][g[1]]+g_v)
elif visit[N-1][M-1]!=-1:
    res=visit[N-1][M-1]
elif visit[g[0]][g[1]]!=-1:
    res=visit[g[0]][g[1]]+g_v

print('Fail' if res<0 or res>T else res)