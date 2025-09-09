N=int(input())
li=list(map(int,input().split()))
dp=[[-1]*(500002) for _ in range(N+1)]
inf=float('inf')
res=0
if N==1:
    print(-1)
elif N==2:
    if li[0]==li[1]:
        print(li[0])
    else:
        print(-1)
else:
    for i in range(N,-1,-1):
        for j in range(500002):
            if j==500001:
                dp[i][j]=-inf
            if i==N:
                if j==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=-inf
            else:
                dp[i][j]=max([dp[i+1][j],dp[i+1][min(500001,j+li[i])],dp[i+1][abs(li[i]-j)]+min(li[i],j)])
    print('-1' if dp[0][0]==0 else dp[0][0])