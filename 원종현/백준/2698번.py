import sys
input=sys.stdin.readline

dp=[[[0,0]for _ in range(102)]for _ in range(102)]
dp[0][1]=[1,1]
for i in range(101):
    for j in range(i+1,101):
        dp[i][j][0]=max(dp[i][j][0],dp[i][j-1][1]+dp[i][j-1][0])
        dp[i][j][1]=max(dp[i][j][1],dp[i-1][j-1][1]+dp[i][j-1][0])


for _ in range(int(input())):
    N,K=map(int,input().split())
    print(sum(dp[K][N]))