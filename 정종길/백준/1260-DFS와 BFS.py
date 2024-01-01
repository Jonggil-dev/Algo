from collections import deque
# DFS 구현
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

# BFS 구현
def bfs(start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]

# 그래프 구성
for _ in range(M) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for connections in graph:
    connections.sort()

visited_dfs = [False] * len(graph)

dfs(V, visited_dfs)
print()
bfs(V)
