from itertools import combinations, product
from bisect import bisect_left, bisect_right

def solution(dice):
    answer = [0, 0]
    n = len(dice)
    idxs = {i for i in range(n)}
    max_win = 0
    combs = combinations(range(n), n // 2)
    
    for comb in combs:
        choice = set(comb)
        other = idxs - choice
        c_dices, o_dices = [], []
        
        for c in choice:
            c_dices.append(dice[c])
        
        for o in other:
            o_dices.append(dice[o])
        
        c_sums = map(sum, product(*c_dices))
        o_candidates = sorted(map(sum, product(*o_dices)))
        
        now_win = 0

        
        for c_sum in c_sums:
            now_win += bisect_left(o_candidates, c_sum)

        if now_win > max_win:
            max_win = now_win
            answer = sorted(choice)
        
    for i in range(len(answer)):
        answer[i] += 1
        
    return answer