import sys
input=sys.stdin.readline

N=int(input())
li=input()
dp=[10**9]*N
dp[0]=0
for i in range(1,N):
    for j in range(i):
        if li[j]=='B' and li[i]=='O':
            dp[i]=min(dp[i],dp[j]+pow(i-j,2))
        elif li[j]=='O' and li[i]=="J":
            dp[i] = min(dp[i],dp[j]+ pow(i-j,2))
        elif li[j]=='J' and li[i]=='B':
            dp[i] = min(dp[i],dp[j]+ pow(i-j,2))

print(dp[N-1] if dp[N-1]!=10**9 else -1)
