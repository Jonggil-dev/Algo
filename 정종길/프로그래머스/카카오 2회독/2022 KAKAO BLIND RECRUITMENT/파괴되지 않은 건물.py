def solution(board, skill):
    answer = 0
    prefix_sums = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            prefix_sums[r1][c1] += -d
            prefix_sums[r2 + 1][c1] += d
            prefix_sums[r1][c2 + 1] += d
            prefix_sums[r2 + 1][c2 + 1] += -d
        else:
            prefix_sums[r1][c1] += d
            prefix_sums[r2 + 1][c1] += -d
            prefix_sums[r1][c2 + 1] += -d
            prefix_sums[r2 + 1][c2 + 1] += d

    for i in range(len(prefix_sums) - 1):
        for j in range(len(prefix_sums[0]) - 2):
            prefix_sums[i][j + 1] += prefix_sums[i][j]
    
    for j in range(len(prefix_sums[0]) - 1):
        for i in range(len(prefix_sums) - 2):
            prefix_sums[i + 1][j] += prefix_sums[i][j]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + prefix_sums[i][j] > 0:
                answer += 1
    return answer