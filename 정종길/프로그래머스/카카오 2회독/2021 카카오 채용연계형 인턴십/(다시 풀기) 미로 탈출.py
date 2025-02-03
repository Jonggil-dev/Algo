import heapq 

def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(1001)]    
    visited = set()
    traps_idx = { t : i for i, t in enumerate(traps)}
    
    for p, q, s in roads:
        graph[p].append((q, s))
        graph[q].append((p, -s))
    
    q = [(0, start, 0)]
    
    while q:
        ans, now, state = heapq.heappop(q)
        visited.add((now, state))
        
        if now == end:
            return ans
        
        here_trap_state = 1
        
        if now in traps_idx:
            state = state ^ (1 << traps_idx[now])
            if (state >> traps_idx[now]) & 1:
                here_trap_state = -1
    
        for next_, dist in graph[now]:
            if (next_, state) not in visited:
                if here_trap_state == 1:
                    if (next_ in traps_idx) and (state >> traps_idx[next_]) & 1:
                        if dist < 0:
                            heapq.heappush(q, (ans + (dist * -1), next_, state))
                    else:
                        if dist > 0:
                            heapq.heappush(q, (ans + dist, next_, state))
                else:
                    if (next_ in traps_idx) and (state >> traps_idx[next_]) & 1:
                        if dist > 0:
                            heapq.heappush(q, (ans + dist, next_, state))
                    else:
                        if dist < 0:
                            heapq.heappush(q, (ans + (dist * -1), next_, state))
        