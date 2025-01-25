from collections import deque

def solution(grid):
    n_row, n_col = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(n_col)] for _ in range(n_row)]
    cycles = []

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_next_direction(i, j, d):
        if grid[i][j] == "L":
            return (d - 1) % 4
        elif grid[i][j] == "R":
            return (d + 1) % 4
        return d

    def bfs(si, sj, sd):
        q = deque([(si, sj, sd)])
        path_length = 0
        visited[si][sj][sd] = True
        while q:
            i, j, d = q.popleft()
            ni, nj = (i + directions[d][0]) % n_row, (j + directions[d][1]) % n_col
            nd = get_next_direction(ni, nj, d)
            if visited[ni][nj][nd]:
                cycles.append(path_length + 1)
                return
            visited[ni][nj][nd] = True
            q.append((ni, nj, nd))
            path_length += 1

    for i in range(n_row):
        for j in range(n_col):
            for d in range(4):
                if not visited[i][j][d]:
                    bfs(i, j, d)

    return sorted(cycles)