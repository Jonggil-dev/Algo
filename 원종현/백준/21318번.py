import sys
input=sys.stdin.readline

N=int(input())
li=[0]+list(map(int,input().split()))
dp=[0]*(N+1)

for i in range(1,N+1):
    dp[i]=dp[i-1]+ (1 if li[i]<li[i-1] else 0)
Q=int(input())
for _ in range(Q):
    x,y=map(int,input().split())
    print(dp[y]-dp[x])
