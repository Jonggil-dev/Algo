def solution(dartResult):
    n = len(dartResult)
    stack, i = [], 0
    
    while i < n:
        if dartResult[i].isdigit():
            if dartResult[i : i + 2] == "10":
                stack.append(int(dartResult[i : i + 2]))
                i += 1
            else:
                stack.append(int(dartResult[i]))
        else:
            if dartResult[i] == "D":
                stack.append(stack.pop() ** 2)
                
            elif dartResult[i] == "T":
                stack.append(stack.pop() ** 3)
                
            elif dartResult[i] == "*":
                now = stack.pop()
                if stack:
                    prev = stack.pop()
                else:
                    prev = 0
                stack.append(prev * 2)
                stack.append(now * 2)

            elif dartResult[i] == "#":
                stack.append(stack.pop() * -1)
        i += 1
            
    return sum(stack)