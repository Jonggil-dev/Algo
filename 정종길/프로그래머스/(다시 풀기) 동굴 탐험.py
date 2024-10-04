from collections import deque

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    
    for start, end in path:
        graph[start].append(end)
        graph[end].append(start)
        
    visited = [0] * n
    ord_info = {} 
    waiting_info = {}
    
    for fst, snd in order:
        ord_info[snd] = fst
    
    q = deque([0])
    visited_cnt = 0
    
    while q:
        here = q.popleft()
        
        if ord_info.get(here, 0) and not visited[ord_info[here]]:
            waiting_info[ord_info[here]] = here
            continue
            
        visited[here] = 1
        visited_cnt += 1
        
        if visited_cnt == n:
            return True
        
        for there in graph[here]:
            if not visited[there]:
                q.append(there)
        
        if here in waiting_info:
            q.append(waiting_info[here])
            
    
    return False