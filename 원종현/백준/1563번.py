import sys
sys.setrecursionlimit(10**8)

def func(a,b,c):
    if b==2 or c==3:
        return 0
    if a==N:
        return 1
    if dp[a][b][c]==-1:
        dp[a][b][c]=func(a+1,b,0)+func(a+1,b+1,0)+func(a+1,b,c+1)
    return dp[a][b][c]

N=int(input())
dp=[[[-1]*3for _ in range(2)] for _ in range(N)]
print(func(0,0,0)%1000000)