def solution(rows, columns, queries):
    global graph, answer
    answer = []
    graph = [[columns * i + j for j in range(1, columns + 1)] for i in range(rows)]
    for r1, c1, r2, c2 in queries:
        rotate(r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    return answer

def rotate(r1, c1, r2, c2):
    global graph, answer
    
    min_v = graph[r1][c1]
    
    for i in range(r1, r2):
        min_v = min(min_v, graph[i + 1][c1])
        graph[i][c1], graph[i + 1][c1] = graph[i + 1][c1], graph[i][c1]
    
    for j in range(c1, c2):
        min_v = min(min_v, graph[r2][j + 1])
        graph[r2][j], graph[r2][j + 1] = graph[r2][j + 1], graph[r2][j]
        
    for i in range(r2, r1, -1):
        min_v = min(min_v, graph[i - 1][c2])
        graph[i][c2], graph[i - 1][c2] = graph[i - 1][c2], graph[i][c2]
    
    for j in range(c2, c1 + 1, -1):
        min_v = min(min_v, graph[r1][j - 1])
        graph[r1][j], graph[r1][j - 1] = graph[r1][j - 1], graph[r1][j]
    
    graph[r1][c1]
    answer.append(min_v)
    return