import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    dp=[0]*(N)
    dp[0]=li[0]
    for i in range(1,N):
        dp[i]=max(dp[i-1]+li[i],li[i])
    print(max(dp))