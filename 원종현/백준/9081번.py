import sys
input=sys.stdin.readline
INF=float('inf')
N,M=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))
res=INF
dp=[[0]*(sum(C)+1) for _ in range(N)]
for i in range(N):
    for j in range(sum(C)+1):
        if j<C[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-C[i]]+A[i],dp[i-1][j])
        if dp[i][j]>=M:
            res=min(res,j)
print(res)
