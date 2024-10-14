from collections import deque

def solution(rc, operations):
    answer = []
    r, c = len(rc), len(rc[0])
    head, body, tail = deque(), deque(), deque()
    
    for i in range(r):
        head.append(rc[i][0])
        body.append(deque(rc[i][1 : c - 1]))
        tail.append(rc[i][-1])
        
    for oper in operations:
        if oper[0] == "S":
            head.appendleft(head.pop())
            body.appendleft(body.pop())
            tail.appendleft(tail.pop())
        else: 
            body[0].appendleft(head.popleft())
            tail.appendleft(body[0].pop())
            body[-1].append(tail.pop())
            head.append(body[-1].popleft())
    
    for i in range(r):
        answer.append([head[i]] + list(body[i]) + [tail[i]])
        
    return answer