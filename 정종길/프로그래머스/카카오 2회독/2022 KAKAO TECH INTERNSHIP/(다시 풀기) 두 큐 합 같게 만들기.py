from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1, queue2 = deque(queue1), deque(queue2)
    
    s1, s2 = sum(queue1), sum(queue2)
    
    
    while s1 != s2:
        
        if s1 > s2:
            a = queue1.popleft()
            queue2.append(a)
            s1 -= a
            s2 += a
            
        elif s1 < s2:
            b = queue2.popleft()
            queue1.append(b)
            s2 -= b
            s1 += b
            
        answer += 1
        
        if answer >= 900000:
            break
        
    if s1 != s2:
        answer = -1
        
    return answer