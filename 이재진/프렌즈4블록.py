def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    d_xy = [(0,1), (1,0), (1,1)]
    while True:
        s = set()
        f = 1
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != -1:
                    now = board[i][j]
                    flag = 1
                    for d in d_xy:
                        ni,nj = i+d[0], j+d[1]
                        if board[ni][nj] != now:
                            flag = 0
                            break
                    if flag:
                        f = 0
                        s.add((i,j))
                        for d in d_xy:
                            ni,nj = i+d[0], j+d[1]
                            s.add((ni,nj))
        if f:
            break
        else:
            for i in s:
                board[i[0]][i[1]] = -1
                answer += 1
            for j in range(n):
                for i in range(m - 1, 0, -1):
                    if board[i][j] == -1:
                        for k in range(i - 1, -1, -1):
                            if board[k][j] != -1:
                                board[i][j] = board[k][j]
                                board[k][j] = -1
                                break
                        
    return answer
