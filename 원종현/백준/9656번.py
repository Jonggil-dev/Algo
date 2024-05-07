N=int(input())
dp=[0]*(N+1)
dp[1]=1
dp[2]=2
dp[1]=1
for i in range(4,N+1):
    if dp[i-1]==1 or dp[i-3]==1:
        dp[i]=2
    else:
        dp[i]=1
print('CY' if dp[N]==1 else 'SK')