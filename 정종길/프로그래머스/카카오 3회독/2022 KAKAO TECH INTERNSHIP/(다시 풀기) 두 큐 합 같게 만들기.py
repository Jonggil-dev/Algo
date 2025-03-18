def solution(queue1, queue2): 
    q = queue1 + queue2
    
    if sum(q) % 2:
        return -1
    else:
        target = sum(q) // 2
        
    s, e = 0, len(queue1) - 1
    now = sum(queue1)
    answer = 0
    
    while s <= e:
        if now == target:  
            return answer
            
        if now < target:
            if e == len(q) - 1:
                break
            e += 1
            now += q[e]
        else:
            now -= q[s]
            s += 1
        answer += 1
    
    return -1