w,h=map(int,input().split())
dp=[[[0]*4 for _ in range(h)] for _ in range(w)]

for i in range(1,w):
    dp[i][0][1]=1
for i in range(1,h):
    dp[0][i][3]=1

for i in range(1,w):
    for j in range(1,h):
        dp[i][j][0]=dp[i-1][j][3]
        dp[i][j][1]=(dp[i-1][j][0]+dp[i-1][j][1])%100000
        dp[i][j][2]=dp[i][j-1][1]
        dp[i][j][3]=(dp[i][j-1][2]+dp[i][j-1][3])%100000
print(sum(dp[w-1][h-1])%100000)

