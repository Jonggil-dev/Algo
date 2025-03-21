import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    w=int(input())
    dp=[0]*(w+1)
    dp[0]=1
    for i in range(N):
        for j in range(li[i],w+1):
            dp[j]+=dp[j-li[i]]
    print(dp[w])