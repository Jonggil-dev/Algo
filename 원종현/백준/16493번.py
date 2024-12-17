N,M=map(int,input().split())
li=[(0,0)]
dp=[[0]*(N+1) for _ in range(M+1)]
for i in range(M):
    a,b=map(int,input().split())
    li.append((a,b))
li.sort()

for i in range(1,M+1):
    for j in range(1,N+1):
        d,p=li[i][0],li[i][1]
        if j < d:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-d]+p)
print(dp[M][N])