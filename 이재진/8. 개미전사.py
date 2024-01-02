import sys
N = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
dp = [0]*101
dp[0] = 0
dp[1] = max(ls[0], ls[1])
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+ls[i])
print(dp[N-1])