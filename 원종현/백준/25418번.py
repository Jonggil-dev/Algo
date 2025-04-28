A,K=map(int,input().split())
dp=[-1]*(K+1)
dp[A]=0
for i in range(A,K+1):
    if i//2>=A and i%2==0:
        dp[i]=min(dp[i//2]+1 if dp[i//2]!=-1 else 10**9,dp[i-1]+1)
    else:
        dp[i]=min(dp[i] if dp[i]!=-1 else 10**9,dp[i-1]+1)
print(dp[K])
