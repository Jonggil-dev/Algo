import heapq

def solution(board):
    n = len(board)
    min_table = [[ [1e9] * 4 for _ in range(n) ] for _ in range(n)]
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    q = []
    
    for i in range(4):
        heapq.heappush(q, (0, (0, 0), i))
        min_table[0][0][i] = 0

    while q:
        cost, (x, y), dt = heapq.heappop(q)
        
        if cost > min_table[x][y][dt]:
            continue
            
        for next_dt in range(4):
            nx, ny = x + dx[next_dt], y + dy[next_dt]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                if next_dt == dt:
                    next_cost = cost + 100
                else:
                    next_cost = cost + 600
                    
                if next_cost < min_table[nx][ny][next_dt]:
                    min_table[nx][ny][next_dt] = next_cost
                    heapq.heappush(q, (next_cost, (nx, ny), next_dt))

    return min(min_table[-1][-1])