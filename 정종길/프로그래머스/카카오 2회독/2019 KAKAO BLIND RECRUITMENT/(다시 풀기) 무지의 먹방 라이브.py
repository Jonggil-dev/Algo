import heapq

def solution(food_times, k):
    answer = 0
    
    h = []
    for idx, f in enumerate(food_times):
        heapq.heappush(h,[f, idx + 1])
    
    turn = last_num = 0
    
    while h:
        remaining_foods = len(h)
        cycle = h[0][0] - last_num
        
        if turn + cycle * remaining_foods > k:
            break
        
        last_num, _ = heapq.heappop(h)
        turn += cycle * remaining_foods
    
    if not h:
        return -1
    
    h.sort(key=lambda x: x[1])

    return h[(k - turn) % len(h)][1]