N=int(input())
li=[]
for i in range(N):
    li.append([int(j) for j in input()])
dp=[[[0]*(10) for _ in range(N)] for _ in range(1<<N)]

def dfs(now,art,cost):
    if dp[now][art][cost]!=0:
        return dp[now][art][cost]
    c=0
    for i in range(1,N)ㅁimport sys

input= sys.stdin.readline
N,M=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]

def func(x,y,c):
    tmp=False
    for i in range(x,N):
        for j in range(y,M):
            if li[i][j]==1:
                li[i][j]=0
                c=c+1+func(i,j,c)
                tmp=True
            if tmp:
                break
        if tmp:
            break
    return c

r=1
for i in range(N+2):
    if r==0:
        print(i-1)
        break
    r=func(i,0,0):
        if li[art][i]>= cost and now&(1<<i)<=0:
            c=max(c,1+dfs(now|1<<i,i,li[art][i]))
    dp[now][art][cost]=c
    return c
print(dfs(1,0,0)+1)