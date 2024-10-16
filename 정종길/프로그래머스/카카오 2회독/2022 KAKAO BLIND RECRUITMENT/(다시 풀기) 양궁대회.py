from itertools import combinations

def solution(n, info):
    global max_diff, answer
    answer = [0] * 11
    apeach = 0

    for i in range(11):
        if info[i]:
            apeach += (10 - i)
    max_diff = 0
    
    for i in range(1, 11):
        for comb in combinations(range(11), i):
            cal_scores(n, info, comb, apeach)
            
    if sum(answer) == 0:
        answer = [-1]
        
    return answer

def cal_scores(n, info, comb, apeach):
    global max_diff, answer
    
    lions = [0] * 11 
    lion = 0
    cnt = n
    
    for idx in sorted(comb):
        if cnt >= (info[idx] + 1):
            lions[idx] += (info[idx] + 1)
            cnt -= (info[idx] + 1)
            lion += (10 - idx)
            if info[idx]:
                apeach -= (10 - idx)
        else:
            return
        
    if max_diff < (lion - apeach):
        max_diff = lion - apeach
        if cnt > 0:
            lions[10] += cnt
        answer = lions
    elif max_diff == (lion - apeach):
        if lion == apeach:
            return
        
        for i in range(10, -1, -1):
            answer[i] < lions[i]
            answer = lions
            break
    return