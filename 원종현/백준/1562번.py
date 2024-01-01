N=int(input())
dp=[[[0 for _ in range(1024)]for _ in range(10)]for _ in range(N)]
# dp[x][y][z] = x자리에서 현재 y숫자를 고른경우, 비트z에 해당하는 숫자들을 방문했을 때

for i in range(1,10):
    dp[0][i][1<<i]=1

for i in range(1,N):
    for k in range(10):
        for z in range(1<<10):
            if k-1>=0:
                dp[i][k][z|(1<<k)]+=dp[i-1][k-1][z]
            if k+1<=9:
                dp[i][k][z|(1<<k)]+=dp[i-1][k+1][z]
            dp[i][k][z|(1<<k)]%=1000000000
res=0
for i in range(10):
    res+=dp[N-1][i][1023]
    res%=1000000000
print(res)