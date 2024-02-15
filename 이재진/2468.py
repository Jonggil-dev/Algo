def bfs(x, y):
    d_ij = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    q = deque()
    q.append((x, y))
    tmp_ls[x][y] = 0
    while q:
        ni, nj = q.popleft()
        for d in d_ij:
            xi, xj = ni + d[0], nj + d[1]
            if 0 <= xi < N and 0 <= xj < N and tmp_ls[xi][xj]:
                q.append((xi, xj))
                tmp_ls[xi][xj] = 0


import sys
import copy
from collections import deque
N = int(sys.stdin.readline())
ls = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_rain = 0
for i in ls:
    if max(i) > max_rain:
        max_rain = max(i)
if max_rain > 100:
    print(0)
else:
    res = 0
    for rain in range(max_rain, -1, -1):
        cnt = 0
        tmp_ls = copy.deepcopy(ls)
        for i in range(N):
            for j in range(N):
                if tmp_ls[i][j] <= rain:
                    tmp_ls[i][j] = 0
        for i in range(N):
            for j in range(N):
                if tmp_ls[i][j]:
                    cnt += 1
                    bfs(i, j)
        if res < cnt:
            res = cnt
    print(res)
