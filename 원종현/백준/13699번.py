N=int(input())
dp=[0]*(36)
dp[0]=1

def func(N):
    global dp
    now=0
    for i in range(0,N):
        if not dp[i]:
            func(i)
        if not dp[N-1-i]:
            func(N-1-i)
        now+=dp[i]*dp[N-i-1]
    dp[N]=now
if N!=0:
    func(N)
print(dp[N])