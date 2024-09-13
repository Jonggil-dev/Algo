from collections import deque, defaultdict

def solution(land):
    answer = defaultdict(int)

    r = len(land)
    c = len(land[0])
    q = deque()
    visited = [[0] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and land[i][j]:
                visited[i][j] = 1
                q.append((i, j))
                column = set()
                cnt = 0
                while q:
                    x, y = q.popleft()
                    column.add(y)
                    cnt += 1
                    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < r and 0 <= ny < c:
                            if not visited[nx][ny] and land[nx][ny]:
                                visited[nx][ny] = 1
                                q.append((nx, ny))
                
                for col in column:
                    answer[col] += cnt

    return max(answer.values())