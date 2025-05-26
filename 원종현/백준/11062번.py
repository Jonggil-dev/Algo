import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    li=list(map(int,input().split()))
    dp=[[0]*(N) for _ in range(N)]

    plag=1 if N%2==1 else 0
    for total_card in range(N):
        for i in range(N-total_card):
            if total_card==0:
                dp[i][i+total_card]=li[i] if plag else 0
            elif plag:
                dp[i][i+total_card]=max(dp[i+1][i+total_card]+li[i],dp[i][i+total_card-1]+li[i+total_card])
            else:
                dp[i][i+total_card]=min(dp[i+1][i+total_card],dp[i][i+total_card-1])
        plag= not plag
    print(dp[0][N-1],dp[0])