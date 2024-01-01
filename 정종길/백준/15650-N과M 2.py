def dfs(start, N, M, sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(start, N + 1):
        if i not in sequence:
            dfs(i + 1, N, M, sequence + [i])



N, M = map(int, input().split())
dfs(1, N, M, [])