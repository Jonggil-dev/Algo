from collections import deque
import copy


def solution(game_board, table):
    answer = 0
    n = len(table)
    puzzles = []
    holes = []

    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                puzzles.append(extract(i, j, table, 1, n))

            if game_board[i][j] == 0:
                holes.append(extract(i, j, game_board, 0, n))

    visited = [0] * len(puzzles)

    for idx, puzzle in enumerate(puzzles):
        if not visited[idx]:
            for _ in range(4):
                if puzzle in holes:
                    answer += len(puzzle)
                    visited[idx] = 1
                    holes.pop(holes.index(puzzle))
                    break

                else:
                    puzzle = normalize(rotate(puzzle))
    return answer


def extract(x, y, arr, num, n):
    q = deque([(x, y)])
    arr[x][y] = 2
    res = [(0, 0)]

    while q:
        i, j = q.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == num:
                    arr[ni][nj] = 2
                    q.append((ni, nj))
                    res.append((ni - x, nj - y))

    res = normalize(res)

    return res


def rotate(puzzle):
    res = []
    for i, j in puzzle:
        res.append((j, -i))
    return res


def normalize(puzzle):
    min_x = min(puzzle, key=lambda x: x[0])[0]
    min_y = min(puzzle, key=lambda x: x[1])[1]

    res = []

    for x, y in puzzle:
        nx, ny = x - min_x, y - min_y
        res.append((nx, ny))

    res.sort(key=lambda x: x[0])
    res.sort(key=lambda x: x[1])
    return res




