from collections import deque


def solution(maps):
    answer = 0
    distance = [[0] * len(maps[0]) for _ in range(len(maps))]

    task = deque([(0, 0)])
    distance[0][0] = 1

    while task:
        i, j = task.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]):
                if maps[ni][nj] and not distance[ni][nj]:
                    distance[ni][nj] = distance[i][j] + 1
                    task.append((ni, nj))

    answer = distance[-1][-1]

    if not answer:
        return -1

    return answer