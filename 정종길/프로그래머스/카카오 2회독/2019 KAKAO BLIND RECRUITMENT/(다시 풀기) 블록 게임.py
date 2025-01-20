from collections import deque, defaultdict

def solution(board):
    answer = 0
    n = len(board)
    q = deque()
    


    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                block = board[i][j]
                visited = set()
                max_x, min_x, max_y, min_y = -1, 50, -1, 50 
                q.append([i, j])
                visited.add((i, j))
                
                while q:
                    x, y = q.popleft()
                    max_x, min_x, max_y, min_y = max(x, max_x), min(x, min_x), max(y, max_y), min(y, min_y)
                    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] == block and (nx, ny) not in visited:
                                q.append([nx, ny])
                                visited.add((nx, ny))
                        
                if delete_block(board, max_x, min_x, max_y, min_y, block):
                    answer += 1
                    
    return answer


def delete_block(board, max_x, min_x, max_y, min_y, block):
    for j in range(min_y, max_y + 1):
        for i in range(max_x, min_x - 1, -1):
            if board[i][j] != 0 and board[i][j] != block:
                return False
            
            if board[i][j] == 0:
                for k in range(i - 1, min_x - 1, -1):
                     if board[k][j] != 0:
                        return False
                
                for l in range(0, min_x):
                    if board[l][j] != 0:
                        return False
                    
                    
    
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            board[i][j] = 0
    

    return True
        

    
    