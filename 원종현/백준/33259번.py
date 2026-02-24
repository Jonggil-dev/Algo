import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li=[0]+[list(map(int,input().split())) for _ in range(N)]
dp=[[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if j<li[i][1]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-li[i][1]]+li[i][0])
res=[dp[N][M],[]]

if res[0]==0:
    print(-1)
else:
    idx=M
    for i in range(N,0,-1):
        if dp[i][idx]!=dp[i-1][idx]:
            res[1].append(i)
            idx-=li[i][1]
    print(len(res[1]))
    print(*sorted(res[1]))