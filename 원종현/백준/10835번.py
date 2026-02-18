import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def func(x,y):
    if x>=N or y>=N:
        return 0
    if dp[x][y]!=-1:
        return dp[x][y]
    if le[x]>ri[y]:
        dp[x][y]=func(x,y+1)+ri[y]
    else:
        tmp_le=func(x+1,y)
        tmp_ri=func(x+1,y+1)
        dp[x][y]=max(tmp_le,tmp_ri)
    return dp[x][y]

N=int(input())
le=list(map(int,input().split()))
ri=list(map(int,input().split()))
dp=[[-1]*N for _ in range(N)]
func(0,0)
print(dp[0][0])