def solution(s):
    global answer, n
    n = answer = len(s)
    
    for i in range(1, (len(s) // 2) + 1):
        res = compression(s, i)
        answer = min(answer, res)
    
    return answer

def compression(s, i):
    global answer, n
    stack = []
    cnt = 1
    
    for j in range(0, n, i):
        head = s[j : j + i]
        if stack and stack[-1] == head:
            cnt += 1
        else:
            if cnt != 1:
                stack.append(str(cnt))
                stack.append(head)
                cnt = 1
            else:
                stack.append(head)
                
    if cnt != 1:
        stack.append(str(cnt))   
            
    return len(''.join(stack))