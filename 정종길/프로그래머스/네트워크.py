from collections import deque

def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i, n, visited, computers)
            answer += 1
    return answer

def bfs(start, n, visited, computers):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        node = queue.popleft()
        for i in range(n):
            if node != i and computers[node][i] and not visited[i]:
                visited[i] = 1
                queue.append(i)
    return

