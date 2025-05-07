N=int(input())
li=list(map(int,input().split()))
dp=[10**9]*(N)
dp[0]=0
for i in range(N):
    for j in range(li[i]+1):
        if i+j<=N-1:
            dp[i+j]=min(dp[i+j],dp[i]+1)
print(dp[N-1] if dp[N-1]!=10**9 else -1)