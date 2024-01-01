# 프로그래머스 캐시

def solution(cacheSize, cities):
    cities = list(map(str.upper, cities)) # 도시 이름 전부 대문자로 만들어버림
    answer = 0
    cache = []
    for city in cities:
        if city not in cache: # 캐시 안에 없으면 miss이므로 +5
            cache.append(city)
            answer += 5
            if len(cache) > cacheSize: # 주어진 캐시 사이즈보다 크면 먼저 들어간거 삭제
                cache.pop(0)
        else: # 캐시 안에 있으면 hit이므로 +1
            cache.remove(city) # 캐시 내부에 있는 city 삭제 후, 뒤에 추가
            cache.append(city)
            answer += 1

    return answer

# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
#
# cacheSize = 2
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
#
# cacheSize = 5
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
#
# cacheSize = 2
# cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
#
# cacheSize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))