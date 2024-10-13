import heapq

def solution(n, paths, gates, summits):
    global distance, is_summit, graph
    
    answer = [0, 1e9]
    distance = [1e9] * (n + 1)
    is_summit = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    for summit in summits:
        is_summit[summit] = 1
    
    for gate in gates:
        daikstra(gate)
    
    summits.sort()
    for summit in summits:
        if answer[1] > distance[summit]:
            answer = [summit, distance[summit]]
    
    return answer

def daikstra(gate):
    global distance, is_summit, graph
    
    q = [(0, gate)]
    distance[gate] = 0

    while q:
        dist, node = heapq.heappop(q)
        
        if (dist > distance[node]) or is_summit[node]:
            continue
        
        for next_, ddist in graph[node]:
            max_ = max(ddist, distance[node])
            if max_ < distance[next_]:
                distance[next_] = max_
                heapq.heappush(q, (ddist, next_))
    