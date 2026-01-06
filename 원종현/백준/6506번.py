import sys
input=sys.stdin.readline

while True:
    N,K=map(int,input().split())
    if N==0 and K==0:
        break
    li=[0]+list(map(int,input().split()))
    dp=[[0]*(K+1) for _ in range(N+1)]
    for i in range(1,N+1):
        dp[i][1]=1
    for i in range(2,N+1):
        for j in range(1,i):
            for k in range(1,K+1):
                if li[i]>li[j]:
                    dp[i][k]+=dp[j][k-1]
    print(dp)
    res=0
    for i in range(1,N+1):
        res+=dp[i][K]
    print(res)