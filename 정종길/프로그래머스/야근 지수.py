import heapq

def solution(n, works):
    answer = 0
    h = []
    if sum(works) <= n:
        return answer
    
    for work in works:
        heapq.heappush(h, -work)
    
    while n > 0:
        num = heapq.heappop(h)
        heapq.heappush(h, num + 1)
        n -= 1
        
    for num in h:
        if num >= 0:
            continue
        answer += num ** 2
        
    return answer