def solution(queries):
    answer = []
    
    for n, p in queries:
        stack = []
        while n > 1:
            p -= 1
            stack.append(p % 4)
            n -= 1
            p = (p // 4) + 1
    
        flag = False
        while stack:
            idx = stack.pop()
            if idx == 0:
                answer.append("RR")
                flag = True
                break
                
            elif idx == 3:
                answer.append("rr")
                flag = True
                break
                
        if flag == False:
            answer.append("Rr")

    return answer