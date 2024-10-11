import sys
sys.setrecursionlimit(5000)


def solution(n, m, x, y, r, c, k):
    global deltas, answer

    deltas = {'r': (0, 1), 'd': (1, 0), 'l': (0, -1), 'u': (-1, 0)}
    answer = ''

    Arr = [[0] * m for _ in range(n)]
    dfs(n, m, x - 1, y - 1, r - 1, c - 1, k, 0, "")

    if not answer:
        answer = "impossible"

    return answer


def dfs(n, m, x, y, r, c, k, cnt, moving):
    global delta, answer
    if abs(x - r) + abs(y - c) > k - cnt or (k - abs(x - r) + abs(y - c) + cnt) % 2:
        return

    if cnt == k:
        if x == r and y == c:
            answer = moving
            return True
        return

    for delta in ['d', 'l', 'r', 'u']:
        nx, ny = x + deltas[delta][0], y + deltas[delta][1]
        if 0 <= nx < n and 0 <= ny < m:
            if dfs(n, m, nx, ny, r, c, k, cnt + 1, moving + delta):
                return True