N,S,M=map(int,input().split())
li=[0]+list(map(int,input().split()))
dp=[[0]*(M+1) for _ in range(N+1)]
dp[0][S]=1
for i in range(1,N+1):
    for j in range(M+1):
        if dp[i-1][j]:
            if 0<=j+li[i]<=M:
                dp[i][j+li[i]]=1
            if 0<=j-li[i]<=M:
                dp[i][j-li[i]]=1
res=-1
for i in range(M,-1,-1):
    if dp[N][i]:
        res=i
        break
print(res)