from collections import deque

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    key_post_order ={}
    
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in order:
        key_post_order[b] = a
    
    q = deque([0])
    waitings = {}
    visited = [0] * n
    
    while q:
        here = q.popleft()
        
        if here in key_post_order and not visited[key_post_order[here]]:
            waitings[key_post_order[here]] = here
            continue
        
                
        visited[here] = 1
        
        if here in waitings:
            q.append(waitings.pop(here))

            
        for next_ in graph[here]:
            if visited[next_]:
                continue
            q.append(next_)
    
    for v in visited:
        if not v:
            return False
    return True
