import sys
input=sys.stdin.readline
d=[0,0,1,-1]
g=[[1,2,3],[4,5,6],[7,8,9],[0,-1,-1]]
dp=[[0]*10 for _ in range(1001)]
for i in range(10):
    dp[1][i]=1
for i in range(1,1000):
    for j in range(10):
        if j==0:
            x,y=3,0
        else:
            x,y=(j-1)//3,(j-1)%3
        for k in range(4):
            dx,dy=x+d[k],y+d[3-k]
            if 0<=dx<=3 and 0<=dy<=2 and g[dx][dy]>-1:
                dp[i+1][g[dx][dy]]=(dp[i+1][g[dx][dy]]+dp[i][j])%1234567

for _ in range(int(input())):
    N=int(input())
    print(sum(dp[N])%1234567)