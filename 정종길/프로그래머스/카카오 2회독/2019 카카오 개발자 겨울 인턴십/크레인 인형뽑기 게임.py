def solution(board, moves):
    answer = 0
    new_board = []
    busket = []
    for col in zip(*board):
        tmp = []
        for num in col[::-1]:
            if num:
                tmp.append(num)
        new_board.append(tmp)
    
    for m in moves:
        if new_board[m - 1]:
            doll = new_board[m - 1].pop()
            if busket and busket[-1] == doll:
                busket.pop()
                answer += 2
            else:
                busket.append(doll)
                
    return answer