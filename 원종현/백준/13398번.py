N=int(input())
li=list(map(int,input().split()))
dp=[[li[i]]*2 for i in range(N)]
for i in range(1,N):
    dp[i][0]=max(dp[i-1][0]+li[i],dp[i][0])
    dp[i][1]=max(dp[i-1][0],dp[i-1][1]+li[i])
r=-10**9
for i in range(N):
    r=max(r,dp[i][0],dp[i][1])
print(r)