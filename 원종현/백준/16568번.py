N,a,b=map(int,input().split())
dp=[10**9]*(1000001)
dp[N]=0
for i in range(N,-1,-1):
    if i-1>=0:
        dp[i-1]=min(dp[i-1],dp[i]+1)
    if i-a-1>=0:
        dp[i-a-1]=min(dp[i-a-1],dp[i]+1)
    if i-b-1>=0:
        dp[i-b-1]=min(dp[i-b-1],dp[i]+1)
print(dp[0])