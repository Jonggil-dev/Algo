import sys
T = int(sys.stdin.readline())
for t in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    ls = []
    for _ in range(N):
        ls.append(int(sys.stdin.readline()))
    dp = [10001] * (M+1)
    dp[0] = 0
    for i in range(N):
        for j in range(ls[i], M+1):
            if dp[j - ls[i]] != 10001:
                dp[j] = min(dp[j], dp[j - ls[i]]+1)
    if dp[M] == 10001:
        res = -1
    else:
        res = dp[M]
    print(f'#{t}', res)