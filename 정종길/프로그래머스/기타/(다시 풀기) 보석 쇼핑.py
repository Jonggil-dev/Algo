from collections import defaultdict

def solution(gems):
    answer = [0, 1000001]
    cnt = defaultdict(int)
    n_type = len(set(gems))
    
    i = j = 0
    cnt[gems[j]] += 1
    
    while i < len(gems) and j < len(gems):
        if len(cnt) < n_type:
            j += 1
            if j == len(gems):
                break
            cnt[gems[j]] += 1
            
        else:
            cnt[gems[i]] -= 1
            if cnt[gems[i]] == 0:
                cnt.pop(gems[i])
                if (answer[1] - answer[0]) > (j - i):
                    answer = [i + 1, j + 1]
            i += 1
        
    return answer