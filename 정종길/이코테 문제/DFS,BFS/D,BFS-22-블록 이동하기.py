from collections import deque

def solution(board):
    global n, answer
    
    n = len(board)
    answer = 1e9
    bfs(board)
    
    return answer

def bfs(board):
    global answer, n
    
    q = deque([[[(0, 0), (0, 1)], 1, 0]])
    tq = deque()
    
    visited = set()
    visited.add(((0, 0), (0, 1)))
    
    while q:
        robot, direction, cnt = q.popleft()
        
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            near_start_i, near_start_j = robot[0][0] + di, robot[0][1] + dj
            near_end_i, near_end_j = robot[1][0] + di, robot[1][1] + dj


            if 0 <= near_start_i < n and 0 <= near_start_j < n and 0 <= near_end_i < n and 0 <= near_end_j < n:
                if not board[near_start_i][near_start_j] and not board[near_end_i][near_end_j]:
                    if (near_start_i, near_start_j) == (n - 1, n - 1) or (near_end_i, near_end_j) == (n - 1, n - 1):
                        answer = min(answer, cnt + 1)
                        continue
                    
                    move_robot = [(near_start_i, near_start_j), (near_end_i, near_end_j)]
                    move_robot.sort(key = lambda x : x[1])
                    move_robot.sort(key = lambda x : x[0])
                    move_robot = tuple(move_robot)
                    
                    if move_robot not in visited:
                        visited.add(move_robot)
                        q.append([move_robot, direction, cnt + 1])
                    
        #direction == 1 이 가로 모양
        tq = deque()
        if direction == 1:
            ti, tj = robot[0][0] + 1, robot[0][1]
            if 0 <= ti < n and 0 <= tj < n:
                if not board[ti][tj]:
                    near_start_i, near_start_j = robot[0][0] + 1, robot[0][1] + 1
                    near_end_i, near_end_j = robot[1][0], robot[1][1]
                    if 0 <= near_start_i < n and 0 <= near_start_j < n and 0 <= near_end_i < n and 0 <= near_end_j < n:
                        tq.append((near_start_i, near_start_j, near_end_i, near_end_j))

            ti, tj = robot[1][0] + 1, robot[1][1]
            if 0 <= ti < n and 0 <= tj < n:
                if not board[ti][tj]:
                    near_start_i, near_start_j = robot[0][0], robot[0][1]
                    near_end_i, near_end_j = robot[1][0] + 1, robot[1][1] -1
                    if 0 <= near_start_i < n and 0 <= near_start_j < n and 0 <= near_end_i < n and 0 <= near_end_j < n:
                        tq.append((near_start_i, near_start_j, near_end_i, near_end_j))
                    
            ti, tj = robot[0][0] - 1, robot[0][1] 
            if 0 <= ti < n and 0 <= tj < n:
                if not board[ti][tj]:
                    near_start_i, near_start_j = robot[0][0] - 1, robot[0][1] + 1
                    near_end_i, near_end_j = robot[1][0], robot[1][1]
                    if 0 <= near_start_i < n and 0 <= near_start_j < n and 0 <= near_end_i < n and 0 <= near_end_j < n:
                        tq.append((near_start_i, near_start_j, near_end_i, near_end_j))
            
            ti, tj = robot[1][0] - 1, robot[1][1] 
            if 0 <= ti < n and 0 <= tj < n:
                if not board[ti][tj]:
                    near_start_i, near_start_j = robot[0][0], robot[0][1]
                    near_end_i, near_end_j = robot[1][0] - 1 , robot[1][1] - 1
                    if 0 <= near_start_i < n and 0 <= near_start_j < n and 0 <= near_end_i < n and 0 <= near_end_j < n:
                        tq.append((near_start_i, near_start_j, near_end_i, near_end_j))
                
            while tq:
                near_start_i, near_start_j, near_end_i, near_end_j = tq.popleft()
                if (near_start_i, near_start_j) == (n - 1, n - 1) or (near_end_i, near_end_j) == (n - 1, n - 1):
                    answer = min(answer, cnt + 1)
                    continue
                    
                move_robot = [(near_start_i, near_start_j), (near_end_i, near_end_j)]
                move_robot.sort(key = lambda x : x[1])
                move_robot.sort(key = lambda x : x[0])
                move_robot = tuple(move_robot)
                if move_robot not in visited:
                    if not board[near_start_i][near_start_j] and not board[near_end_i][near_end_j]:
                        visited.add(move_robot)
                        q.append([move_robot, 0, cnt + 1])

        else:
            ti, tj = robot[0][0], robot[0][1] + 1
            if 0 <= ti < n and 0 <= tj < n:
                if not board[ti][tj]:
                    near_start_i, near_start_j = robot[0][0] + 1, robot[0][1] + 1
                    near_end_i, near_end_j = robot[1][0], robot[1][1]
                    if 0 <= near_start_i < n and 0 <= near_start_j < n and 0 <= near_end_i < n and 0 <= near_end_j < n:
                        tq.append((near_start_i, near_start_j, near_end_i, near_end_j))
                
            ti, tj = robot[1][0], robot[1][1] + 1
            if 0 <= ti < n and 0 <= tj < n:
                if not board[ti][tj]:
                    near_start_i, near_start_j = robot[0][0], robot[0][1]
                    near_end_i, near_end_j = robot[1][0] - 1, robot[1][1] + 1
                    if 0 <= near_start_i < n and 0 <= near_start_j < n and 0 <= near_end_i < n and 0 <= near_end_j < n:
                        tq.append((near_start_i, near_start_j, near_end_i, near_end_j))
            
                            
            ti, tj = robot[0][0], robot[0][1] - 1
            if 0 <= ti < n and 0 <= tj < n:
                if not board[ti][tj]:
                    near_start_i, near_start_j = robot[0][0] + 1, robot[0][1] - 1
                    near_end_i, near_end_j = robot[1][0], robot[1][1]
                    if 0 <= near_start_i < n and 0 <= near_start_j < n and 0 <= near_end_i < n and 0 <= near_end_j < n:
                        tq.append((near_start_i, near_start_j, near_end_i, near_end_j))

            ti, tj = robot[1][0], robot[1][1] - 1
            if 0 <= ti < n and 0 <= tj < n:
                if not board[ti][tj]:
                    near_start_i, near_start_j = robot[0][0], robot[0][1]
                    near_end_i, near_end_j = robot[1][0] - 1, robot[1][1] - 1
                    if 0 <= near_start_i < n and 0 <= near_start_j < n and 0 <= near_end_i < n and 0 <= near_end_j < n:
                        tq.append((near_start_i, near_start_j, near_end_i, near_end_j))
                
            while tq:
                near_start_i, near_start_j, near_end_i, near_end_j = tq.popleft()
                
                if (near_start_i, near_start_j) == (n - 1, n - 1) or (near_end_i, near_end_j) == (n - 1, n - 1):
                    answer = min(answer, cnt + 1)
                    continue
                    
                move_robot = [(near_start_i, near_start_j), (near_end_i, near_end_j)]
                move_robot.sort(key = lambda x : x[1])
                move_robot.sort(key = lambda x : x[0])
                move_robot = tuple(move_robot)
                if move_robot not in visited:
                    if not board[near_start_i][near_start_j] and not board[near_end_i][near_end_j]:
                        visited.add(move_robot)
                        q.append([move_robot, 1, cnt + 1])

                
            