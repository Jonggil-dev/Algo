N=int(input())
P=list(map(int,input().split()))
M=int(input())
dp=[-1]*(M+1)

for i in range(N-1,-1,-1):
    now=P[i]
    for j in range(now,M+1):
        dp[j]=max(dp[j-now]*10+i,i,dp[j])
print(dp[M])