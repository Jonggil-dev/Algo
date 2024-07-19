N=int(input())
dp=[0]*(N+1)
dp[1]=0

def func(now):
    if dp[now]:
        return dp[now]
    for i in range(1,now):
        left=func(i)
        right=func(now-i)
        dp[now]=max(dp[now],left+right+i*(now-i))
    return dp[now]
func(N)
print(dp[N])