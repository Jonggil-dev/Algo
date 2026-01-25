T=int(input())

k=0
coin=[1,10,25]
while T:
    T-=1
    N=int(input())
    res=0
    dp=[float('inf')]*100
    dp[0]=0
    for i in coin:
        for j in range(i,100):
            dp[j]=min(dp[j],dp[j-i]+1)
    while N:
        res+=dp[N%100]
        N//=100
    print(res)