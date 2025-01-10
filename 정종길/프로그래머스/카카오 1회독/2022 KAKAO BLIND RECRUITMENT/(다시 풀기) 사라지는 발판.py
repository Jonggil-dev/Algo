def solution(board, aloc, bloc):
    global r, c
    r, c = len(board), len(board[0])
    
    ar, ac = aloc
    br, bc = bloc
    _, answer = play(board, ar, ac, br, bc)
    
    return answer 

def play(board, my_r, my_c, opponent_r, opponent_c):
    global r, c
    
    if board[my_r][my_c] == 0:
        return (False, 0)
    
    board[my_r][my_c] = 0
    min_win = 1e9
    max_lose = 0
    
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        my_nr, my_nc = my_r + dr, my_c + dc
        if 0 <= my_nr < r and 0 <= my_nc < c and board[my_nr][my_nc]:
            result, turn = play(board, opponent_r, opponent_c, my_nr, my_nc)
            
            if result:
                max_lose = max(max_lose, turn + 1) 
            else:
                min_win = min(min_win, turn + 1)
    
    board[my_r][my_c] = 1
    
    if min_win < 1e9:
        return (True, min_win)
    else:
        return (False, max_lose)
                