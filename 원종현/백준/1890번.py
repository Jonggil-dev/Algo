N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
dp=[[0]*(N) for _ in range(N)]
dp[0][0]=1
for i in range(N):
    for j in range(N):
        now=li[i][j]
        if not now or not dp[i][j]:
            continue
        if i+now<N:
            dp[i+now][j]+=dp[i][j]
        if j+now<N:
            dp[i][j+now]+=dp[i][j]
print(dp[N-1][N-1])