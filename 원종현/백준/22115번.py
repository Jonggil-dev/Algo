N,K=map(int,input().split())
li=[0]+list(map(int,input().split()))
dp=[[100000]*(K+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0]=0
for i in range(1,N+1):
    for j in range(1,K+1):
        if j<li[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=min(dp[i-1][j],dp[i-1][j-li[i]]+1)
print(-1 if dp[N][K]==100000 else dp[N][K])