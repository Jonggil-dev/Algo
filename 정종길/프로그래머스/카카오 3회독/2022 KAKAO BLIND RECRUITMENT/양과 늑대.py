'''
최악의 연산 횟수 러프하게 (2 ^ N) * N
(1) 각 노드의 방문 상태 (방문함, 방문안함) -> 2 ^ N
(2) 각 노드에 방문했을 때 별로 (1)의 방문 상태를 가질 수 있으므로 -> (2 ^ N) * N 
''' 

def solution(info, edges):
    global answer, graph
    
    answer = 1
    graph = [[] for _ in range(17)]
    
    for p, s in edges:
        graph[p].append(s)
    
    dfs(0, 1, 0, set(graph[0]), info)
    
    return answer

def dfs(now, sheep, wolf, nexts, info):
    global answer, graph
    
    answer = max(answer, sheep)
    
    for n in nexts:
        new_sheep, new_wolf = sheep, wolf
        if info[n]:
            if sheep <= wolf + 1:
                continue
                
            new_wolf += 1
            
        else:
            new_sheep += 1
            
        cnexts = nexts.copy()
        cnexts.remove(n)
        cnexts |= set(graph[n])
        dfs(n, new_sheep, new_wolf, cnexts, info)