import sys
input=sys.stdin.readline

def func(a,b):
    if b==(1<<N)-1:
        return 1
    if ~dp[a][b]:
        return dp[a][b]
    dp[a][b]=0
    for j in range(N):
        if not b&(1<<j) and abs(H[a]-H[j]) >K:
            dp[a][b]+=func(j,b|(1<<j))
    return dp[a][b]

N,K=map(int,input().split())
H=[]
for i in range(N):
    H.append(int(input()))
dp=[[-1]*(1<<N) for _ in range(N)]
res=0
for i in range(N):
    res+=func(i,1<<i)
print(res)