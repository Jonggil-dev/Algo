import sys
input=sys.stdin.readline
INF=int(1e9)
N=int(input())
li=[[0,0,0]]+[list(map(int,input().split())) for _ in range(N)]
dp=[[[INF]*3 for _ in range(3)] for _ in range(N+1)]
# dp[i][j][k] = i번째집을 j색으로 색칠하는데 시작점은 k일때,
for i in range(3):
    dp[1][i][i]=li[1][i]
for i in range(2,N):
    for j in range(3):
        dp[i][0][j]=min(dp[i-1][1][j],dp[i-1][2][j])+li[i][0]
        dp[i][1][j]=min(dp[i-1][0][j],dp[i-1][2][j])+li[i][1]
        dp[i][2][j]=min(dp[i-1][0][j],dp[i-1][1][j])+li[i][2]
res=10**9
for i in range(3):
    dp[N][0][i]=INF if (i==0) else min(dp[N-1][1][i],dp[N-1][2][i])+li[N][0]
    dp[N][1][i]=INF if (i==1) else min(dp[N-1][0][i],dp[N-1][2][i])+li[N][1]
    dp[N][2][i]=INF if (i==2) else min(dp[N-1][0][i],dp[N-1][1][i])+li[N][2]

res=INF
for i in range(3):
    res=min(res,min(dp[N][i]))
print(res)
