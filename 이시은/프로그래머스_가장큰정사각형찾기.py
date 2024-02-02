# 프로그래머스 가장 큰 정사각형 찾기
def solution(board):
    n_row = len(board)
    n_col = len(board[0])
    MAX = 1

    dp = [[0] * (n_col + 1) for _ in range(n_row + 1)]
    if sum([sum(line) for line in board]) == 0:
        return 0
    if n_row == n_col and sum([sum(line) for line in board]) == n_col**2:
        return n_col**2

    for r in range(1, n_row+1):
        for c in range(1, n_col+1):
            if board[r-1][c-1] == 1:
                dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                MAX = max(dp[r][c], MAX)
    return MAX ** 2


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[0,0,1,1],[1,1,1,1]]
board = [[0,0,0,1,1,1],[0,0,0,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]

print(solution(board))