import heapq
def solution(x, y, n):
    
    q = [(0, x)]
    visited = set()
    
    while q:
        cnt, num = heapq.heappop(q)
        
        if num == y:
            return cnt
        
        if num > y:
            continue
        
        for nnum in (num * 3, num * 2, num + n):
            if nnum not in visited:
                heapq.heappush(q, (cnt + 1, nnum))
                visited.add(nnum)
    return -1