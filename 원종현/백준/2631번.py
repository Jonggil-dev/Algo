N=int(input())
li=[0]+[int(input()) for _ in range(N)]
dp=[1]*(N+1)
for i in range(1,N+1):
    for j in range(1,i):
        if li[j]<li[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(N-max(dp))