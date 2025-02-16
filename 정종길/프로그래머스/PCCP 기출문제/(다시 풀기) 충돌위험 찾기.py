from collections import defaultdict, deque

def solution(points, routes):
    answer = 0
    
    infos = {}
    for idx, (x, y) in enumerate(points): 
        infos[idx + 1] = (x, y)
        
    q = []
    for route in routes:
        q.append((infos[route[0]], deque( [infos[num] for num in route[1:]])))
        
    while q:
        tmp = []
        crash = defaultdict(int)
        
        for now, target in q:
            crash[now] += 1
            
            if now == target[0]:
                target.popleft()
                if not target:
                    continue
            
            tmp.append(moving(now, target))
            
        for cnt in crash.values():
            if cnt >= 2:
                answer += 1
        
        q = tmp
        
    return answer

def moving(now, target):
    nx, ny = now[0], now[1]
    tx, ty = target[0][0], target[0][1]
    
    if nx != tx:
        if nx > tx:
            return ((nx - 1, ny), target)
        else:
            return ((nx + 1, ny), target)
    else:
        if ny > ty:
            return ((nx, ny - 1), target)
        else:
            return ((nx, ny + 1), target)
        