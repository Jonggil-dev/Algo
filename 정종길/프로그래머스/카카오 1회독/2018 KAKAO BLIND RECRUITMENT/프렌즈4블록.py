def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    
    while True:
        blocks = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j]:
                    word = board[i][j]
                    if board[i][j + 1] == word and board[i + 1][j] == word and board[i + 1][j + 1] == word:
                        blocks.add((i, j))
                        blocks.add((i, j + 1))
                        blocks.add((i + 1, j))
                        blocks.add((i + 1, j + 1))
                        
        if not blocks:
            break
            
        else:
            answer += len(blocks)
            
            for i, j in blocks:
                board[i][j] = 0
                
            for col in range(n):
                for row in range(m - 1, -1, -1):
                    if board[row][col]:
                        idx = row + 1
                        while idx < m and not board[idx][col]:
                            board[idx - 1][col], board[idx][col] = board[idx][col], board[idx - 1][col]
                            idx += 1
    return answer