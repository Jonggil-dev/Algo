# 프로그래머스 혼자서 하는 틱택토

# 올바른 게임이 아닌 경우 (게임은 항상 O가 먼저 시작한다)
# 1. O의 개수 > X의 개수+1
# 2. O의 개수 < X의 개수
# 3. O가 한 줄이 되는 경우가 있는데(O가 승리하는 경우), O가 X보다 한 개 더 많지 않은 경우
# 4. X가 한 줄이 되는 경우가 있는데(X가 승리하는 경우), O와 X의 개수가 같지 않은 경우
def solution(board):
    cnt_o, cnt_x = 0, 0
    # 숫자로 기록하는 보드 => O: 1, X: 10, . = 0
    n_board = [[0] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                cnt_o += 1
                n_board[i][j] = 1
            elif board[i][j] == 'X':
                cnt_x += 1
                n_board[i][j] = 10

    if cnt_o < cnt_x or cnt_o > cnt_x+1:
        return 0
    
    for k in range(3):
        if (sum(n_board[k]) == 3 or sum(list(zip(*n_board))[k]) == 3) and cnt_o != cnt_x + 1:
                return 0
        if (sum(n_board[k]) == 30 or sum(list(zip(*n_board))[k]) == 30) and cnt_o != cnt_x:
                return 0

        
    if n_board[0][0] + n_board[1][1] + n_board[2][2] == 3 and cnt_o != cnt_x + 1:
        return 0
    
    if n_board[0][0] + n_board[1][1] + n_board[2][2] == 30 and cnt_o != cnt_x:
        return 0
    
    if n_board[0][2] + n_board[1][1] + n_board[2][0] == 3 and cnt_o != cnt_x + 1:
        return 0

    if n_board[0][2] + n_board[1][1] + n_board[2][0] == 30 and cnt_o != cnt_x:
        return 0
            
    return 1


board = ["O.X", ".O.", "..X"]
board = ["OOO", "...", "XXX"]
board = ["...", ".X.", "..."]
board = ["...", "...", "..."]
print(solution(board))