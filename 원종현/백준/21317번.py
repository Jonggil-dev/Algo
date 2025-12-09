import sys
input=sys.stdin.readline
INF=float('inf')
N=int(input())
li=[[0,0] for _ in range(N+1)]
for i in range(1,N):
    a,b=map(int,input().split())
    li[i][0]=a
    li[i][1]=b
K=int(input())
if N==1:
    print(0)
    exit()

dp=[[INF,INF] for _ in range(N+1)]
dp[0]=[0,0]
dp[1][0]=0

if N>=2:
    dp[2]=[li[1][0],INF]
if N>=3:
    dp[3]=[min(li[1][0]+li[2][0],li[1][1]),INF]

for i in range(4,N+1):
    dp[i][0]=min(dp[i-1][0]+li[i-1][0],dp[i-2][0]+li[i-2][1])
    dp[i][1]=min(dp[i-3][0]+K,dp[i-2][1]+li[i-2][1],dp[i-1][1]+li[i-1][0])

print(min(dp[N]))