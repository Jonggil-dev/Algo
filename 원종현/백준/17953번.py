N,M=map(int,input().split())
li=[[0]*(M) for _ in range(N)]
for i in range(M):
    v=list(map(int,input().split()))
    for j in range(N):
        li[j][i]=v[j]

dp=[[0]*(M) for _ in range(N)]
for i in range(M):
    dp[0][i]=li[0][i]

for i in range(1,N):
    for j in range(M):
        v=0
        for k in range(M):
            if k==j:
                continue
            v=max(v,li[i][j]+dp[i-1][k])
        dp[i][j]=max(v,dp[i][j],li[i][j]//2+dp[i-1][j])
print(max(dp[N-1]))