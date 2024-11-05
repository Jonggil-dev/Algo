def solution(s):
    answer = 1e9
    if len(s) == 1:
        return 1
    
    for i in range(1, (len(s) // 2) + 1):
        stack = []
        cnt = 1
        for j in range(0, len(s), i):
            word = s[j : j + i]
            if stack and stack[-1] == word:
                cnt += 1
            else:
                if cnt == 1:
                    stack.append(word)
                else:
                    stack.append(str(cnt))
                    stack.append(word)
                    cnt = 1
                    
        if cnt > 1:
            stack.append(str(cnt))
            
        answer = min(answer, len(''.join(stack)))
        
    return answer