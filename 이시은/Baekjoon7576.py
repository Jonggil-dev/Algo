# Baekjoon 7576 토마토
# 시간초과

import sys
from collections import deque

input = sys.stdin.readline
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def BFS(start):
    queue = deque()
    queue.append(start)
    visited = [[False] * M for _ in range(N)]
    while queue:
        r, c = queue.popleft()
        visited[r][c] = True
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < M) and not visited[nr][nc]:
                visited[nr][nc] = True
                if MAP[nr][nc] == 0:
                    MAP[nr][nc] = MAP[r][c] + 1
                    queue.append([nr, nc])
                elif MAP[nr][nc] == -1:
                    continue
                else:
                    MAP[nr][nc] = min(MAP[r][c] + 1, MAP[nr][nc])
                    queue.append([nr, nc])


M, N = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

ripes = []
isAllRipe = True
for row in range(N):
    if 0 in MAP[row]:
        isAllRipe = False
    for col in range(M):
        if MAP[row][col] == 1:
            ripes.append([row, col])

if isAllRipe:
    print(0)

else:
    for ripe in ripes:
        BFS(ripe)

    for line in MAP:
        if 0 in line:
            print(-1)
            break
    else:
        print(max([max(MAP[row]) for row in range(N)]) - 1)