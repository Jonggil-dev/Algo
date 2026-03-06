import sys
input=sys.stdin.readline
INF=float('inf')
N,M,A,B=map(int,input().split())
dp=[INF]*(N+1)
dp[0]=0
for i in range(M):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        dp[j]=-1

for i in range(1,N+1):
    if dp[i]<0:
        continue

    tmpa,tmpb=i-A,i-B
    if 0<=tmpa and dp[tmpa]!=-1:
        dp[i]=min(dp[tmpa]+1,dp[i])
    if 0<=tmpb and dp[tmpb]!=-1:
        dp[i]=min(dp[tmpb]+1,dp[i])

print(-1 if dp[N]==INF else dp[N])