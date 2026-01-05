N=int(input())
li=list(map(int,input().split()))
res=0
for i in range(-99,100):
    dp=[0]*101
    for j in range(N):
        if 0<li[j]-i<101:
            dp[li[j]]=max(dp[li[j]],dp[li[j]-i]+1)
        else:
            dp[li[j]]=1
    res=max(res,max(dp))
print(res)
