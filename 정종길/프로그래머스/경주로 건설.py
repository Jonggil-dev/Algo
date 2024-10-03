import heapq

def solution(board):
    answer = 0
    r, c = len(board), len(board[0])
    visited = set()
    q = []

    heapq.heappush(q, (0, 0, 0, 0))
    heapq.heappush(q, (0, 0, 0, 1))
    
    while q:
        pay, i, j, direct = heapq.heappop(q)
        if (i, j) == (r - 1, c - 1):
            return pay
        
        if (i, j, direct) in visited:
            continue

        visited.add((i, j, direct))
        for idx, (di, dj) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
            ni, nj = i + di, j + dj
            if 0 <= ni < r and 0 <= nj < c:
                if not board[ni][nj] and (ni, nj, idx) not in visited:
                    if idx == direct:
                        n_pay = pay + 100
                        
                    else:
                        n_pay = pay + 600
                        
                    heapq.heappush(q, (n_pay, ni, nj, idx))
                    
    return pay