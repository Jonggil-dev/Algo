import sys
input=sys.stdin.readline

dp=[1,2,4,7]
tmp=4
for i in range(int(input())):
    N=int(input())
    for j in range(len(dp),N):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[N-1])