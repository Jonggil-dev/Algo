from collections import deque
def solution(queue1, queue2):
    answer = -1
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    for _ in range(4*len(queue1)):
        if sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            cnt += 1
        elif sum1 < sum2:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            cnt += 1
        else:
            return cnt
            
    return answer
