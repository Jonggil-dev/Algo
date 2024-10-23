from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        cnt = defaultdict(int)
        for order in orders:
            for comb in combinations(sorted(order), c):
                cnt["".join(comb)] += 1

        if cnt and max(cnt.values()) >= 2:
            mv = max(cnt.values())
        else:
            continue
        

        for k, v in cnt.items():
            if v == mv:
                answer.append(k)
        
        answer.sort()
        
    return answer