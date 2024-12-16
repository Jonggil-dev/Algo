N=int(input())
M=int(input())
dp=[[0]*M for i in range(N)]
dp[0]=[1]*M
for i in range(1,N):
    dp[i][i]=1
    for j in range(i+1,M):
        dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
print(dp[-1][-1])