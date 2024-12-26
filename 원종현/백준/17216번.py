import sys
input=sys.stdin.readline

N=int(input())
li=list(map(int,input().split()))
dp=li[:]
for i in range(N):
    for j in range(i):
        if li[j]>li[i]:
            dp[i]=max(dp[i],dp[j]+li[i])
print(max(dp))