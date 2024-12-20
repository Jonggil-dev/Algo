N=int(input())
li=[[0]*(101) for _ in range(101)]
for i in range(N):
    a,b=map(int,input().split())
    li[a][b]=1
    li[b][a]=1

dp=[[0]*(101) for _ in range(101)]
for i in range(1,100):
    for j in range(1,101-i):
        for k in range(j,j+i):
            dp[j][j+i]=max(dp[j][j+i],dp[j][k]+dp[k][j+i]+li[j][j+i])
print(dp[1][100])