from collections import defaultdict
def solution(board, moves):
    answer = 0
    stack = []
    row_info = defaultdict(int)
    
    l = len(board)
    
    for i in range(l):
        for j in range(l):
            if board[i][j]:
                if not row_info[j + 1]:
                    row_info[j + 1] = i + 1
    
    for k in range(l + 1):
        if not row_info[k]:
            row_info[k] = l + 1
    
    for move in moves:
        r = row_info[move]
        if r == l + 1:
            continue
            
        num = board[r - 1][move - 1]
        if stack and (stack[-1] == num):
            stack.pop()
            answer += 2
        else:
            stack.append(num)
        row_info[move] += 1
            
    return answer