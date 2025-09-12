from collections import deque,Counter
import sys
input=sys.stdin.readline
d1=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
d2=[(0,1),(0,-1),(1,0),(-1,0)]
N,M=map(int,input().split())
li=[input().rstrip() for _ in range(N)]
visit=[[0]*(M) for _ in range(N)]
land=[[]]

def func(x):
    if res[x]!=-1:
        return res[x]
    dep=1
    for i in graph2[x]:
        dep=max(func(i)+1,dep)
    res[x]=dep
    return dep

cnt=0
# 섬 index 기록 및 각 섬땅 기록(land)
for i in range(N):
    for j in range(M):
        if li[i][j]=='x' and not visit[i][j]:
            q=deque([])
            q.append((i,j))
            cnt+=1
            visit[i][j]=cnt
            land.append([])
            land[cnt].append((i,j))
            while q:
                x,y=q.popleft()
                for dx,dy in d1:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<N and 0<=ny<M and li[nx][ny]=='x' and not visit[nx][ny]:
                        visit[nx][ny]=cnt
                        land[cnt].append((nx,ny))
                        q.append((nx,ny))

visit2=[[0]*(M) for _ in range(N)]
check=[0]*(51)
q=deque([])
graph=[-1]*(cnt+1)
tar=set()
graph2=[set() for _ in range(cnt+1)]

for i in range(N):
    for j in range(M):
        if ((i==0 or i==N-1) or (j==0 or j==M-1)) and li[i][j]=='.':
            q.append((i,j))
            visit2[i][j]=1
        elif ((i==0 or i==N-1) or (j==0 or j==M-1)) and li[i][j]=='x':
            graph[visit[i][j]]=1
            visit2[i][j]=1
            tar.add(visit[i][j])

while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+d2[i][0],y+d2[i][1]
        if 0<=nx<N and 0<=ny<M and not visit2[nx][ny] and li[nx][ny]=='x':
            tar.add(visit[nx][ny])
            visit2[nx][ny]=1
            graph[visit[nx][ny]]=1
        elif 0<=nx<N and 0<=ny<M and not visit2[nx][ny] and li[nx][ny]=='.':
            q.append((nx,ny))
            visit2[nx][ny]=1

while tar:
    next_tar=set()
    for now in tar:
        q=deque([])
        for x,y in land[now]:
            q.append((x,y))
            visit2[x][y]=1
        while q:
            x,y=q.popleft()
            for dx,dy in d2:
                nx,ny=x+dx,y+dy
                if 0<=nx<N and 0<=ny<M and not visit2[nx][ny] and li[nx][ny]=='x':
                    if visit[nx][ny]==now:
                        q.append((nx,ny))
                        visit2[nx][ny]=1
                    else:
                        graph2[now].add(visit[nx][ny])
                        next_tar.add(visit[nx][ny])
                elif 0<=nx<N and 0<=ny<M and not visit2[nx][ny] and li[nx][ny]=='.':
                    q.append((nx,ny))
                    visit2[nx][ny]=1

    tar=list(next_tar)

res=[-1]*(cnt+1)
for i in range(1,cnt+1):
    func(i)

if cnt==0:
    print(-1)
else:
    max_dep=max(res[1:cnt+1])
    if max_dep<=0:
        print(-1)
    else:
        tmp=[0]*(max_dep)
        for i in range(1,cnt+1):
            if res[i]>0:
                tmp[res[i]-1]+=1
        print(*tmp)