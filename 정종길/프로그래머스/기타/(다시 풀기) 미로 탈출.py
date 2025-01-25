import heapq as hq

def solution(n, start, end, roads, traps):
    edges = [[] for _ in range(n + 1)]

    trap_idx = {t : n for n, t in enumerate(traps)}
    traps = set(traps)
	
    for v1, v2, w in roads:
        edges[v1].append((v2, w))
        edges[v2].append((v1, -w))
	
    heap = [(0, start, 0)]
    dist = {}

    while heap:
        dis, here, state = hq.heappop(heap)
        
        if here == end:
            return dis
        
        if dist.get((here, state), None):
            continue
            
        dist[(here, state)] = dis
    
        direction = 1
        
        if here in traps and (state & (1 << trap_idx[here])):
            direction *= -1

        for there, w in edges[here]:
            if there in traps and (state & (1 << trap_idx[there])):
                w *= -1
                
            if w * direction > 0:
                new_state = state
                if there in traps:
                    if state & (1 << trap_idx[there]):
                        new_state = state & ~(1 << trap_idx[there])
                    else: 
                        new_state = state | (1 << trap_idx[there]) 

                hq.heappush(heap, (dis + w * direction, there, new_state))
    return -1