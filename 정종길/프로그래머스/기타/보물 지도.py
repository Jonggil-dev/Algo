from collections import deque

def solution(n, m, hole):
    global graph, visited
    
    graph = [[0] * m for _ in range(n)]
    for r, c in hole:
        graph[r - 1][c - 1] = 1
        
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    
    answer = bfs(n, m)
        
    return answer

def bfs(n, m):
    global graph, visited
    
    q = deque([(0, 0, False)])
    visited[0][0][0] = True
    L = 0
    
    while q:
        for _ in range(len(q)):
            x, y, is_jump = q.popleft()
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) == ((n - 1), (m - 1)):
                        return L + 1;
                    
                    if not visited[nx][ny][is_jump] and not graph[nx][ny]:
                        visited[nx][ny][is_jump] = True
                        q.append((nx, ny, is_jump))
                    
                if not is_jump:
                    jx, jy = x + 2 * dx, y + 2 * dy
                    if 0 <= jx < n and 0 <= jy < m:
                        if (jx, jy) == ((n - 1), (m - 1)):
                            return L + 1;
                        
                        if not visited[jx][jy][1] and not graph[jx][jy]:
                            visited[jx][jy][1] = True
                            q.append((jx, jy, True))     
        L += 1
        
    return -1