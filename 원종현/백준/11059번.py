S=input()
N=len(S)
res=0
li=[int(i) for i in S]
dp=[0]*(N+1)
for i in range(1,N+1):
    dp[i]=dp[i-1]+li[i-1]
for i in range(2,N+1,2):
    for j in range(N-i+1):
        mid=j+i//2
        f=dp[mid]-dp[j]
        b=dp[j+i]-dp[mid]
        if f==b:
            res=max(res,i)
print(res)