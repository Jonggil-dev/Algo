N,K=map(int,input().split())
dp=[float('inf')]*(N+1)
dp[0]=0

for i in range(1,N+1):
    dp[i]=min(dp[i],dp[i-1]+1)
    if i+i//2<=N:
        dp[i+i//2]=min(dp[i+i//2],dp[i]+1)
print('minigimbob' if dp[-1]<=K else 'water')