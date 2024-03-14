N=int(input())
li=[]
for i in range(N):
    li.append([int(j) for j in input()])
dp=[[[0]*(10) for _ in range(N)] for _ in range(1<<N)]

def dfs(now,art,cost):
    if dp[now][art][cost]!=0:
        return dp[now][art][cost]
    c=0
    for i in range(1,N):
        if li[art][i]>= cost and now&(1<<i)<=0:
            c=max(c,1+dfs(now|1<<i,i,li[art][i]))
    dp[now][art][cost]=c
    return c
print(dfs(1,0,0)+1)