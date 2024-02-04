N,K=map(int,input().split())
li=[]
dp=[10**9]*(K+1)
dp[0]=0
for i in range(N):
    s=int(input())
    for j in range(s,K+1):
        dp[j]=min(dp[j-s]+1,dp[j])
print(dp[K] if dp[K]!=10**9 else -1)