import sys
from collections import deque
N = int(sys.stdin.readline())
ls = [list(sys.stdin.readline().strip()) for _ in range(N)]
res = 0
def bfs(i, j):
    q = deque()
    q.append((i,j))
    d_ij = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    cnt = 0
    while q:
        ni, nj = q.popleft()
        cnt += 1
        ls[ni][nj] = '0'
        for d in d_ij:
            ki, kj = ni + d[0], nj + d[1]
            if 0 <= ki < N and 0 <= kj < N and ls[ki][kj] != '0' and (ki, kj) not in q:
                q.append((ki, kj))
    return cnt

home_cnt = []
for i in range(N):
    for j in range(N):
        if ls[i][j] != '0':
            res += 1
            home_cnt.append(bfs(i, j))
print(res)
for h in sorted(home_cnt):
    print(h)
