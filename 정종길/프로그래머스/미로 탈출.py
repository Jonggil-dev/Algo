from collections import deque


def solution(maps):
    global n_row, n_col
    answer = 0
    n_row = len(maps)
    n_col = len(maps[0])

    for i in range(n_row):
        for j in range(n_col):
            if maps[i][j] == "S":
                si, sj = i, j

            elif maps[i][j] == "L":
                li, lj = i, j

            elif maps[i][j] == "E":
                ei, ej = i, j

    tmp = bfs(si, sj, li, lj, maps)

    if tmp:
        answer += tmp
    else:
        return -1

    tmp = bfs(li, lj, ei, ej, maps)
    if tmp:
        answer += tmp
    else:
        return -1

    return answer


def bfs(si, sj, ei, ej, arr):
    global n_row, n_col

    visited = [[0] * n_col for _ in range(n_row)]
    q = deque([(si, sj)])

    while q:
        i, j = q.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < n_row and 0 <= nj < n_col:
                if arr[ni][nj] != "X" and not visited[ni][nj]:
                    visited[ni][nj] += (visited[i][j] + 1)
                    q.append((ni, nj))

    return visited[ei][ej]