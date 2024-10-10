def game(board, p):
        for i in range(3):
            if board[i][0] == p:
                if board[i][1] == p and board[i][2] == p:
                    return True
        for i in range(3):
            if board[0][i] == p:
                if board[1][i] == p and board[2][i] == p:
                    return True
        
        if board[0][0] == p and board[1][1] == p and board[2][2] == p:
            return True
        if board[0][2] == p and board[1][1] == p and board[2][0] == p:
            return True

def solution(board):
    answer = 1
    o_cnt = 0
    x_cnt = 0
    for i in board:
        for j in i:
            if j == "O":
                o_cnt += 1
            elif j == "X":
                x_cnt += 1
    if o_cnt - x_cnt not in [0,1]:
        return 0
        
    if game(board, "O"):
        if o_cnt - x_cnt != 1:
            return 0
    
    if game(board, "X"):
        if o_cnt != x_cnt:
            return 0
    
    return answer
