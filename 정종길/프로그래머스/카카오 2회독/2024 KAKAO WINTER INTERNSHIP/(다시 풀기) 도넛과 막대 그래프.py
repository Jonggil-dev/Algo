from collections import deque, defaultdict

def solution(edges):
    max_node = max(max(edges, key = lambda x : x[0])[0], max(edges, key = lambda x : x[1])[1])
    in_graph = [[] for _ in range(max_node + 1)]
    out_graph = [[] for _ in range(max_node + 1)]
    find_start = defaultdict(int)
    
    for s, e in edges:
        in_graph[e].append(s)
        out_graph[s].append(e)
        find_start[e] += 1
        find_start[s] -= 1
    
    for k, v in find_start.items():
        if v <= -2:
            s = k
            break
            
    answer = [s, 0, 0, 0]
    
    q = deque([s])
    visited  = [0] * (max_node + 1)
    
    while q:
        here = q.popleft()
        
        for there in out_graph[here]:
            if len(out_graph[there]) == 2:
                answer[3] += 1
                continue
                
            elif len(out_graph[there]) == 0:
                answer[2] += 1
                continue
            
            elif visited[there]:
                answer[1] += 1
                continue
            
            else:
                visited[there] = 1
                q.append(there)
                
    return answer

