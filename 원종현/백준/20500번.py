N=int(input())
dp=[0]*(N+1)
for i in range(2,N+1):
    if i%2:
        dp[i]=(dp[i-1]*2-1)%1000000007
    else:
        dp[i]=(dp[i-1]*2+1)%1000000007
print(dp[N])