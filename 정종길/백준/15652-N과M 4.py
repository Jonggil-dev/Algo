def solve(depth, start, N, M, result):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    for i in range(start, N + 1):
        result[depth] = i
        solve(depth + 1, i, N, M, result)

N, M = map(int, input().split())
result = [0] * M
solve(0, 1, N, M, result)