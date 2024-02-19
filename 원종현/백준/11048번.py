N,M=map(int,input().split())
li=[[0]*(M+1)]
for i in range(N):
    li.append([0]+list(map(int,input().split())))
dp=[[0]*(M+1) for i in range(N+1)]
dp[1][1]=li[1][1]
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j]=max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+li[i][j]
print(dp[N][M])
