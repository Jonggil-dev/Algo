import sys
input=sys.stdin.readline

C,N=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(N)]
dp=[10**9 for _ in range(C+101)]
dp[0]=0

for c,p in li:
    for i in range(p,C+101):
        dp[i]=min(dp[i],dp[i-p]+c)
print(min(dp[C:]))