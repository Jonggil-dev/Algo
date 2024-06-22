N=int(input())
dp=[0,0,1]
tmp=2

if N>2:
    for i in range(3,N+1):
        dp.append(((dp[i-1]+dp[i-2])*(i-1))%1000000007)
        tmp*=i
    print((tmp*dp[N])%1000000007)
else:
    if N==1:
        print(0)
    else:
        print(2)