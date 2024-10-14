from collections import deque

def solution(rc, operations):
    answer = []
    r, c = len(rc), len(rc[0])
    left, body, right = deque(), deque(), deque() 

    for row in rc:
        left.append(row[0])
        body.append(deque(row[1:-1]))
        right.append(row[-1])
    
    for operation in operations:
        if operation[0] == "S":
            body.appendleft(body.pop())
            left.appendleft(left.pop())
            right.appendleft(right.pop())
        else:
            body[0].appendleft(left.popleft())
            right.appendleft(body[0].pop())
            body[-1].append(right.pop())
            left.append(body[-1].popleft())
            
    for i in range(r):
        answer.append([left[i]] + list(body[i]) + [right[i]])
    
    
    return answer