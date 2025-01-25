def solution(m, n, board):
    answer = 0
    board = [list(text) for text in board]
    
    while True:
        blocks = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    blocks.add((i, j))
                    blocks.add((i + 1, j))
                    blocks.add((i, j + 1))
                    blocks.add((i + 1, j + 1))
                    
        if not blocks:
            break
        
        else:
            answer += len(blocks)
        
            for k, l in blocks:
                board[k][l] = 0
            
            for j in range(n):
                for i in range(1, m):
                    if board[i][j] == 0:
                        while 0 < i:
                            board[i - 1][j], board[i][j] = board[i][j], board[i - 1][j]
                            i -= 1
    return answer