N = int(input())
M = int(input())

default=list(int(input()) for _ in range(M))

dp=[[0]*2 for _ in range(N+1)]

dp[1][0]=1
dp[1][1]=0


for d in default:
    dp[d][1]=-1

for i in range(2,N+1):
    if dp[i][1]==-1:
        if dp[i-1][1]!=-1:
            dp[i][0]=dp[i-1][0]+dp[i-1][1]
            dp[i][1]=-1
        else:
            dp[i][0]=dp[i-1][0]
            dp[i][1]=-1
    else:
        if dp[i-1][1]!=-1:
            dp[i][0]=dp[i-1][0]+dp[i-1][1]
            dp[i][1]=dp[i-1][0]
        else:
            dp[i][0]=dp[i-1][0]
            dp[i][1]=0

if dp[N][1]==-1:
    print(dp[N][0])
else:
    print(dp[N][0]+dp[N][1])