N=int(input())

if N==1:
    print(2)
elif N==2:
    print(7)
else:
    dp=[0]*(N+1)
    A=[0]*(N+1)
    B=[0]*(N+1)
    dp[1]=2
    dp[2]=7
    A[1],B[1]=1,1
    for i in range(3,N+1):
        A[i-1]=dp[i-2]+B[i-2]
        B[i-1]=dp[i-2]+A[i-2]
        dp[i]=(dp[i-1]*2+dp[i-2]+A[i-1]+B[i-1])%1000000007

    print(dp[N])
