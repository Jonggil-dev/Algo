from collections import deque

def solution(menu, order, k):
    answer = 0
    ord_info = deque()
    ord_time = -k
    fin_time = 0
    
    for idx in order:
        ord_time += k
        if fin_time <= ord_time:
            fin_time = (ord_time + menu[idx])
        else:
            fin_time += menu[idx]
        ord_info.append((ord_time, fin_time))

    while ord_info:
        waiting = 1
        ord_time, fin_time = ord_info.popleft()
        
        for nord_time, nfin_time in ord_info:
            if nord_time < fin_time:
                waiting += 1
            else:
                break
                
        answer = max(answer, waiting)

    return answer