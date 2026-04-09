import sys
input=sys.stdin.readline

N,M,K,T=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(M)]
li.sort(key=lambda x:(x[0],x[1]))
time=[0]*(N+1)
for a,b in li:
    for i in range(a,b):
        time[i]+=1
dp=[[[0]*(K+1) for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(K+1):
        for k in range(j+1):
            if time[i]>=T:
                dp[i][j][0]=max(dp[i][j][0],dp[i-1][j][k]+1)
            else:
                v=max(0,T-time[i])
                if k>=v:
                    dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k]+1)
                else:
                    v2=v-k
                    if K>=j+v2:
                        dp[i][j+v2][v]=max(dp[i][j+v2][v],dp[i-1][j][k]+1)
                    dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k])

res=0
for i in range(K+1):
    for j in range(K+1):
        res=max(res,dp[N][i][j])
print(res)
