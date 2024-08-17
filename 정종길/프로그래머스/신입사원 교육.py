import heapq

def solution(ability, number):
    answer = 0
    li = []
    for num in ability:
        heapq.heappush(li, num)

    while number > 0:
        number -= 1
        x = heapq.heappop(li)
        y = heapq.heappop(li)
        heapq.heappush(li, x + y)
        heapq.heappush(li, x + y)

    answer = sum(li)

    
    return answer