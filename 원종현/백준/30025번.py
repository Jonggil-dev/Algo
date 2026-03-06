N,M,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
dp=[0]*(K+1)

for i in range(N):
    if A[i]!=0:
        dp[A[i]%K]+=1

print(dp)

for _ in range(1,M):
    tmp=[0]*(K+1)
    for i in range(K):
        for j in range(N):
            now=(10*i+A[j])%K
            tmp[now]+=dp[i]
    dp=tmp
print(dp[0]%1000000007)