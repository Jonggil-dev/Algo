import sys
input=sys.stdin.readline
v=10**6+1
dp=[0]*v
for i in range(1,10**3+1):
    dp[i*i]=1
for i in range(2,v):
    if not dp[i]:
        for j in range(1,10**3+1):
            if i+j*j>=v-1:
                break
            dp[i+j*j]=1
for _ in range(int(input())):
    N=int(input())
    print('koosaga' if dp[N] else 'cubelover')