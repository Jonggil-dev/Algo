import math
N=int(input())
def func(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
so=[]
for i in range(2,N+1):
    if func(i):
        so.append(i)
dp=[0]*(N+1)
dp[0]=1
for i in so:
    for j in range(i,N+1):
        dp[j]=(dp[j]+dp[j-i])%123456789
print(dp[N])