from pprint import pprint


def solution(board, skill):
    answer = 0
    row, col = len(board), len(board[0])
    prefix_table = [[0] * (col + 1) for _ in range(row + 1)]
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d = -d
        prefix_table[r1][c1] += d
        prefix_table[r1][c2 + 1] += -d
        prefix_table[r2 + 1][c1] += -d
        prefix_table[r2 + 1][c2 + 1] += d

    for i in range(row + 1):
        for j in range(col):
            prefix_table[i][j + 1] += prefix_table[i][j]

    for i in range(col + 1):
        for j in range(row):
            prefix_table[j + 1][i] += prefix_table[j][i]

    for i in range(row):
        for j in range(col):
            if (board[i][j] + prefix_table[i][j]) > 0:
                answer += 1

    return answer