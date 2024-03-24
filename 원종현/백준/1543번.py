N=int(input())
li=[0]+list(map(int,input().split()))
dp=[0 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(i):
        if li[j]<li[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))