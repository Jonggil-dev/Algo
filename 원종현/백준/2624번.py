import sys
input=sys.stdin.readline

T=int(input())
K=int(input())
li=[]
dp=[0]*(T+1)
dp[0]=1

for i in range(K):
    p,n=map(int,input().split())
    li.append((p,n))

for coin,c in li:
    for j in range(T,0,-1):
        for k in range(1,c+1):
            if j-coin*k>=0:
                dp[j]+=dp[j-coin*k]
print(dp[T])