from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = set()       
    order = deque()     
    answer = 0

    for city in cities:
        city = city.lower()

        if city in cache:
            answer += 1
            order.remove(city)
            order.append(city)


        else:
            answer += 5
            if len(cache) >= cacheSize:  
                oldest = order.popleft() 
                cache.remove(oldest)

            cache.add(city)
            order.append(city)

    return answer
