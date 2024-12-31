N,M,K=map(int,input().split())
res=-10**9
li=[list(map(int,input().split())) for _ in range(N)]
d=[[1,0],[-1,0],[0,1],[0,-1]]
visit=[[0]*(M) for _ in range(N)]
def func(g,val,x,y):
    global res
    if g==K:
        res=max(res,val)
        return
    for i in range(x,N):
        for j in range(y if x==i else 0,M):
            if visit[i][j]:
                continue
            for nx,ny in d:
                if 0<=i+nx<N and 0<=j+ny<M and visit[i+nx][j+ny]:
                    break
            else:
                visit[i][j]=1
                func(g+1,val+li[i][j],i,j)
                visit[i][j]=0
func(0,0,0,0)
print(res)