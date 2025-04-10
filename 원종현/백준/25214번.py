N=int(input())
li=list(map(int,input().split()))
dp=[[0,10**9]]
for i in range(1,N+1):
    dp.append([max(dp[i-1][0],li[i-1]-dp[i-1][1]),min(dp[i-1][1],li[i-1])])
for i in range(1,N+1):
    print(dp[i][0],end=' ')