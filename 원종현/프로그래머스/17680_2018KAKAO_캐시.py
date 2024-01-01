def solution(cacheSize, cities):
    answer = 0
    cache=[0]*(cacheSize)
    for i in range(len(cities)):
        city=cities[i].lower()
        if city not in cache:
            answer+=5
            if cacheSize!=0:
                cache.pop(0)
        else:
            answer+=1
            if cacheSize!=0:
                cache.pop(cache.index(city))
        if cacheSize!=0:
            cache.append(city)
    return answer