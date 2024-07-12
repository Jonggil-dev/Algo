import sys
input=sys.stdin.readline


T,W=map(int,input().split())
li=[0]
for i in range(T):
    li.append(int(input()))
dp=[[0]*(W+1) for _ in range(T+1)]
dp[1][0]=li[1]%2
dp[1][1]=li[1]//2
for i in range(2,T+1):
    for j in range(W+1):
        k=li[i]%2 if j%2==0 else li[i]//2
        dp[i][j]=max(dp[i-1][0:j+1])+k
print(max(dp[-1]))