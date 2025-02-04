from collections import defaultdict

def solution(gems):
    nows = defaultdict(int)
    kinds = len(set(gems))
    n = len(gems)
    answer = [1, n]
    i = j = 0
    
    while j < n:
        jurely = gems[j]
        nows[jurely] += 1
        
        while len(nows) == kinds and i <= j:
            jurely = gems[i]
            nows[jurely] -= 1
            
            if not nows[jurely]:
                if (j - i) < (answer[1] - answer[0]):
                    answer[0], answer[1] = i + 1, j + 1
                nows.pop(jurely)
                
            i += 1
        j += 1
    
    return answer