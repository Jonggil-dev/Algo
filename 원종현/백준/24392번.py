import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li=[list(map(int,input().split())) for i in range(N)]
dp=[[0]*M for _ in range(N)]
dp[0]=li[0]
for i in range(N-1):
    for j in range(M):
        if li[i][j]==0:
            continue
        for k in range(j-1,j+2):
            if 0<=k<M and li[i+1][k]==1:
                dp[i+1][k]+=dp[i][j]
print(sum(dp[N-1])%1000000007)