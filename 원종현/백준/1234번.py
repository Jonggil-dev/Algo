from math import factorial
N,R,G,B=map(int,input().split())

dp=[{} for _ in range(N+1)]
dp[0][(0,0,0)]=1
def comb(x,y):
    return factorial(x)//factorial(y)//factorial(x-y)
for i in range(1,N+1):
    for xr,xg,xb in dp[i-1].keys():
        nr,ng,nb=R-xr,G-xg,B-xb
        cnt=dp[i-1][(xr,xg,xb)]
        if i%3==0 and i//3<=min([nr,ng,nb]):
            c=cnt*(factorial(i))//(factorial(i//3)**3)
            if (xr+i//3,xg+i//3,xb+i//3) not in dp[i]:
                dp[i][(xr+i//3,xg+i//3,xb+i//3)]=c
            else:
                dp[i][(xr+i//3,xg+i//3,xb+i//3)]+=c
        if i%2==0:
            c=cnt*(factorial(i))//(factorial(i//2)**2)
            if i//2<=min([nr,ng]):
                if (xr+i//2,xg+i//2,xb) not in dp[i]:
                    dp[i][(xr+i//2,xg+i//2,xb)]=c
                else:
                    dp[i][(xr+i//2,xg+i//2,xb)]+=c
            if i//2<=min([nr,nb]):
                if (xr+i//2,xg,xb+i//2) not in dp[i]:
                    dp[i][(xr+i//2,xg,xb+i//2)]=c
                else:
                    dp[i][(xr+i//2,xg,xb+i//2)]+=c
            if i//2<=min([ng,nb]):
                if (xr,xg+i//2,xb+i//2) not in dp[i]:
                    dp[i][(xr,xg+i//2,xb+i//2)]=c
                else:
                    dp[i][(xr,xg+i//2,xb+i//2)]+=c

        if i<=nr:
            if (xr+i,xg,xb) not in dp[i]:
                dp[i][(xr+i,xg,xb)]=cnt
            else:
                dp[i][(xr+i,xg,xb)]+=cnt
        if i<=ng:
            if (xr,xg+i,xb) not in dp[i]:
                dp[i][(xr,xg+i,xb)]=cnt
            else:
                dp[i][(xr,xg+i,xb)]+=cnt
        if i<=nb:
            if (xr,xg,xb+i) not in dp[i]:
                dp[i][(xr,xg,xb+i)]=cnt
            else:
                dp[i][(xr,xg,xb+i)]+=cnt
res=sum([i for i in dp[N].values()])
print(res)
