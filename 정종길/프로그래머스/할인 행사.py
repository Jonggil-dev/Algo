from collections import defaultdict

def solution(want, number, discount):
    global answer
    answer = 0
    
    wants = defaultdict(int)
    tmp = defaultdict(int)
    
    for i in range(len(want)):
        wants[want[i]] += number[i]

    for j in range(10):
        if discount[j] in wants:
            tmp[discount[j]] += 1
            
    check(wants, tmp)
    
    for k in range(1, len(discount) - 9):
        if discount[k - 1] in wants:
            tmp[discount[k - 1]] -= 1
            
        if discount[k + 9] in wants:
            tmp[discount[k + 9]] += 1

        check(wants, tmp)
        
    return answer

def check(wants, tmp):
    global answer
    
    for k, v in wants.items():
        if not k in tmp:
            return
        
        if tmp[k] != v:
            return

    answer += 1
    return