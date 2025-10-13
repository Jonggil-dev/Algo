import sys
input=sys.stdin.readline

N,T=map(int,input().split())
li=[]
for _ in range(N):
    d,m=map(int,input().split())
    li.append((d,m))
val=(sum([m for d,m in li]))
dp=[[0]*(T+1) for _ in range(N+1)]
for i in range(1,T+1):
    for j in range(1,N+1):
        d,m=li[j-1]
        if i>=d:
            dp[j][i]=max(dp[j-1][i],dp[j-1][i-d]+m)
        else:
            dp[j][i]=dp[j-1][i]
print(val-dp[N][T])