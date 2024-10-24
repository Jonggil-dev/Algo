def solution(n, s, a, b, fares):
    graph = [[float('INF')] * (n + 1) for _ in range(n + 1)]
    answer = 1e9
    
    for i in range(1, n + 1):
        graph[i][i] = 0
        
    for st, en, d in fares:
        graph[st][en] = d
        graph[en][st] = d
    
    
    for k in range(1, n + 1): 
        for i in range(1, n + 1): 
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

                
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
        
    return answer