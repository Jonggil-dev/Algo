import heapq
from collections import deque
def solution(program):

    program.sort(key= lambda x:x[0])
    program.sort(key= lambda x:x[1])
    programs = deque(program)
    waitings = []
    answer = [0] * 11
    
    time = program[0][1] + program[0][2]
    programs.popleft()
    
    while programs:
        a, b, c = programs.popleft()
        
        if b <= time:
            heapq.heappush(waitings, (a, b, c))
            
        else:
            if not waitings:
                time = b + c
                continue
            
            flag = False
            
            while waitings:
                na, nb, nc = heapq.heappop(waitings)
                answer[na] += (time - nb)
                time += nc
                
                if time >= b:
                    heapq.heappush(waitings, (a, b, c))
                    flag = True
                    break
                    
            if not flag:
                time = b + c
                
    while waitings:
        na, nb, nc = heapq.heappop(waitings)
        answer[na] += (time - nb)
        time += nc
    answer[0] = time
    
    return answer