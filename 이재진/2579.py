import sys
N = int(sys.stdin.readline())
ls = [0] + [int(sys.stdin.readline()) for _ in range(N)]
dp = [0]*(N+1)
dp[1] = ls[1]
if N > 1:
    dp[2] = ls[1] + ls[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-2], dp[i-3]+ls[i-1]) + ls[i]
print(dp[N])