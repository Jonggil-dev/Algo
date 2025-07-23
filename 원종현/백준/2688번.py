for i in range(int(input())):
    N=int(input())
    dp=[1]*(10)

    for i in range(N-1):
        for j in range(10):
            dp[j]=sum(dp[j:])
    print(sum(dp))