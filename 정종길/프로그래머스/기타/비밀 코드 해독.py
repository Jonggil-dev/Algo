from itertools import combinations

def solution(n, q, ans):
    answer = 0
    combs = combinations(range(1, n+1), 5)
    q = [set(row) for row in q]
    
    for comb in list(combs):
        if match(comb, q, ans):
            answer += 1
            
    return answer

def match(comb, q, ans):
    for i in range(len(q)):
        right_cnt = 0
        for n in comb:
            if n in q[i]:
                right_cnt += 1
        
        if right_cnt != ans[i]:
            return False

    return True
    