def solution(cap, n, deliveries, pickups):
    answer = 0
    i = j = n - 1
    
    while i >= 0 or j >= 0:
        box_d = box_p = 0
        max_d = max_p = -1
        
        # 박스 배달
        while i >= 0:
            if deliveries[i]:
                max_d = max(max_d, i)
                box_d += deliveries[i]
                if box_d <= cap:
                    deliveries[i] = 0
                else:
                    deliveries[i] = box_d - cap
                    break
            else:
                i -= 1

         # 박스 수거
        while j >= 0:
            if pickups[j]:
                max_p = max(max_p, j)
                box_p += pickups[j]
                if box_p <= cap:
                    pickups[j] = 0
                else:
                    pickups[j] = box_p - cap
                    break
            else:
                j -= 1
        
        answer += 2 * (max(max_d, max_p) + 1)
        
    return answer