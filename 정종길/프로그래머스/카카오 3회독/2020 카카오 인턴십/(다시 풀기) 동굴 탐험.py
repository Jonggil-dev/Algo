'''
2회차 풀이가 더 깔끔함
'''
from collections import deque

def solution(n, path, order):
    unlocks, afters = {}, set()
    visited = [0] * n
    graph = [[] for _ in range(n)]
    
    for pre, after in order:
        unlocks[pre] = after
        afters.add(after)

    for s, e in path:
        graph[s].append(e)
        graph[e].append(s)
    
    
    waitings = set()
    q = deque([0])
    
    while q:
        now = q.popleft()
        if now in afters and now not in waitings:
            waitings.add(now)
            continue
        
        visited[now] = 1
        
        if now in unlocks:
            if unlocks[now] in waitings:
                q.append(unlocks[now])
            else:
                waitings.add(unlocks[now])
            
        for next_ in graph[now]:
            if not visited[next_]:
                q.append(next_)

                
    for v in visited:
        if v == 0:
            return False
            
    return True