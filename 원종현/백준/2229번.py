N=int(input())
li=list(map(int,input().split()))
dp=[0]*N
for i in range(1,N):
    for j in range(1,i+2):
        tmp=li[i-j+1:i+1]
        if j==i+1:
            j=i
        dp[i]=max(dp[i],dp[i-j]+abs(max(tmp)-min(tmp)))
print(dp[-1])
