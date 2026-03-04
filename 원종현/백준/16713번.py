import sys
input=sys.stdin.readline

N,Q=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(N+1)
res=0
for i in range(1,N+1):
    dp[i]=dp[i-1]^a[i-1]

for i in range(Q):
    s,e=map(int,input().split())
    res^=dp[e]^dp[s-1]
print(res)