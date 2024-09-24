from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        if city.upper() in q:
            answer += 1
            q.remove(city.upper())
            q.append(city.upper())
        else:
            answer += 5
            if len(q) >= cacheSize:
                q.popleft()
            q.append(city.upper())
            
    return answer