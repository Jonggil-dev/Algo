import heapq

def solution(n, paths, gates, summits):
    answer = [0, 1e9]
    summits = set(summits)
    intensities = [1e9] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    for gate in gates:
        q = [(0, gate)]
        intensities[gate] = 0
        
        while q:
            w, h = heapq.heappop(q)
            
            if w > intensities[h]:
                continue
            
            if h in summits:
                if w < answer[1]:
                    answer = [h, w]
                elif w == answer[1]:
                    if h < answer[0]:
                        answer = [h, w]
                continue
            
            for t, tw in graph[h]:
                dist = max(w, tw)
                if dist < intensities[t]:
                    intensities[t] = dist
                    heapq.heappush(q, (dist, t))
                    
    return answer