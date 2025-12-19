N=int(input())
li=list(map(int,input().split()))

dp=[10**9]*N
dp[0]=0
for i in range(1,N):
    for j in range(i):
        dp[i]=min(max(dp[j],(i-j)*(1+abs(li[i]-li[j]))),dp[i])
print(dp[N-1])