def solution(n, s, a, b, fares):
    answer = 1e9
    graph = [[1e9] * (n + 1) for _ in range(n + 1)]
    
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if r == c:
                graph[r][c] = 0
                
    for x, y, w in fares:
        graph[x][y] = w
        graph[y][x] = w
    
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                                  
    for l in range(1, n + 1):
        answer = min(answer, graph[s][l] + graph[l][a] + graph[l][b])
    
    return answer