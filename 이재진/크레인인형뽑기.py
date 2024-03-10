def solution(board, moves):
    answer = 0
    ls = [0]
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]:
                ls.append(board[i][m-1])
                board[i][m-1] = 0
                if ls[-1] == ls[-2]:
                    ls.pop()
                    ls.pop()
                    answer += 2
                break
    return answer
