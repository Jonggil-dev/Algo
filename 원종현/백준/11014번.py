import sys
input=sys.stdin.readline
d=[(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

def func(x,y):
    if visit[x][y]:
        return 0
    visit[x][y]=1
    for nx,ny in li[x][y]:
        if check[nx][ny]==-1 or func(*check[nx][ny]):
            check[nx][ny]=(x,y)
            return 1
    return 0

C=int(input())
for _ in range(C):
    N,M=map(int,input().split())
    S=[]
    li=[[[] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        s=input().rstrip()
        S.append(s)
    for x in range(N):
        for y in range(0,M,2):
            if S[x][y]!='.':
                continue
            for dx,dy in d:
                nx,ny=x+dx,y+dy
                if 0<=nx<N and 0<=ny<M and S[nx][ny]=='.':
                    li[x][y].append((nx,ny))
    check=[[-1]*M for _ in range(N)]
    res=sum([sum([1 for j in i if j=='.'])   for i in S])
    for x in range(N):
        for y in range(0,M,2):
            if li[x][y]:
                visit=[[0]*M for _ in range(N)]
                res-=func(x,y)
    print(res)