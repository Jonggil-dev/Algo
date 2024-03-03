def solution(board, h, w):
    color = board[h][w]
    dij = [(0,1), (1,0), (0,-1), (-1,0)]
    answer = 0
    for i,j in dij:
        ni = h+i
        nj = w+j
        if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == color:
            answer += 1
    return answer
