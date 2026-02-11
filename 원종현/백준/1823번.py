import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def func(st,end,c):
    if st==end:
        return c*li[st]
    if dp[st][end]:
        return dp[st][end]
    dp[st][end]=max(func(st+1,end,c+1)+c*li[st],func(st,end-1,c+1)+c*li[end])
    return dp[st][end]

N=int(input())
li=[int(input()) for _ in range(N)]
dp=[[0]*N for _ in range(N)]
print(func(0,N-1,1))