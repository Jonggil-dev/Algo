import sys
input=sys.stdin.readline

N,M=map(int,input().split())

dp=[0]*(M+1)
li=[]
for i in range(N):
    V,C,K=map(int,input().split())

    idx=1
    while K>0:
        t=min(idx,K)
        li.append((V*t,C*t))
        idx*=2
        K-=t
for i in range(len(li)):
    V,C=li[i]
    for j in range(M,-1,-1):
        if j>=V:
            dp[j]=max(dp[j-V]+C,dp[j])
print(max(dp))

