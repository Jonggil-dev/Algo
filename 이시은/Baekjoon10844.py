# Baekjoon 10844 쉬운 계단 수

"""
이렇게 하면 시간 초과

import sys

input = sys.stdin.readline

N = int(input())
answer = 0

def DP(length, last):
    global answer
    if last < 0 or last > 9:
        return

    if length == 1:
        answer += 1
        return

    DP(length - 1, last - 1)
    DP(length - 1, last + 1)

for i in range(1, 10):
    DP(N, i)

print(answer%1000000000)
"""

# DP => 앞의 결과를 이용해서 뒤의 결과를 구함

import sys

input = sys.stdin.readline

N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)