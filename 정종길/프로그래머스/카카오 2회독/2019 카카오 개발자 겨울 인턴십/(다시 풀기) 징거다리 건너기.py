def solution(stones, k):
    answer = 0
    s, e = min(stones), max(stones) + 1
    
    while s < e:
        mid = (s + e) // 2
        
        i = 0
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0

        if cnt >= k:
            e = mid
        else:
            answer = mid
            s = mid + 1

    return answer