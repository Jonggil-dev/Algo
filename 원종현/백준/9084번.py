import sys
input=sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    M=int(input())
    dp=[0]*(M+1)
    dp[0]=1
    for i in li:
        for j in range(M+1):
            if j>=i:
                dp[j]+=dp[j-i]
    print(dp[M])