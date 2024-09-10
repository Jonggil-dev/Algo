import heapq


def algo(board, start, end):
    dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dis = [[float("inf")] * len(board[0]) for _ in range(len(board))]
    pq = [[0, start[0], start[1]]]
    dis[start[0]][start[1]] = 0
    while pq:
        w, ci, cj = heapq.heappop(pq)
        if ci == end[0] and cj == end[1]:
            return w

        if dis[ci][cj] >= w:
            for di, dj in dij:
                ni, nj = ci, cj
                if di == 0:
                    while True:
                        if 0 <= nj + dj < len(board[0]) and board[ni][nj + dj] != "D":
                            nj += dj
                        else:
                            break

                elif dj == 0:
                    while True:
                        if 0 <= ni + di < len(board) and board[ni + di][nj] != "D":
                            ni += di
                        else:
                            break
                if ni != ci or nj != cj:
                    if dis[ni][nj] > w + 1:
                        dis[ni][nj] = w + 1
                        heapq.heappush(pq, [w + 1, ni, nj])
    return -1


def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                start = [i, j]
            elif board[i][j] == "G":
                end = [i, j]
    ans = algo(board, start, end)
    return ans
