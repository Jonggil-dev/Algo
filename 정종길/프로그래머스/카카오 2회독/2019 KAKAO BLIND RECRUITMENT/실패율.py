from collections import defaultdict

def solution(N, stages):
    answer = []
    records = defaultdict(int)
    p = len(stages)
    
    res = []
    
    for k in stages:
        records[k] += 1
    
    for i in range(1, N + 1):
        if p > 0 :
            res.append((records[i] / p , i))
            p -= records[i]
        else:
            res.append((0 , i))
        
    for _, j in sorted(res, key = lambda x : (-x[0], x[1])):
        answer.append(j)
    
    return answer