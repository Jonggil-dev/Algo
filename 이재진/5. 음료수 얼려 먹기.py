d_xy = [(0,1), (1,0), (0,-1), (-1,0)]
def dfs(now):
    if ls[now[0]][now[1]] == 1:
        return
    ls[now[0]][now[1]] = 1
    for d in d_xy:
        next = (now[0]+d[0], now[1]+d[1])
        if 0 <= next[0] < N and 0 <= next[1] < M:
            dfs(next)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ls = [list(map(int, list(input()))) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ls[i][j] == 0:
                cnt += 1
                dfs((i,j))
    print(f'#{t}', cnt)