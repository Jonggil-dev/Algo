import sys
T = int(sys.stdin.readline())
for t in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[float("inf")] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        graph[i][i] = 0
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1
        graph[b][a] = 1
    X, K = map(int, sys.stdin.readline().split())
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                graph[j][k] = min(graph[j][k], graph[i][j] + graph[i][k])
    res = graph[1][K] + graph[X][K]
    if res >= float("inf"):
        res = -1
    print(f'#{t}', res)