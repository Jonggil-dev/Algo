from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    combs = combinations(range(n), n // 2)
    max_win = 0
    
    for comb in combs:
        A_dices = []
        B_sums = []
        win = 0
        
        for a_idx in comb:
            A_dices.append(dice[a_idx])
        
        B_dices = [dice[b_idx] for b_idx in range(n) if b_idx not in comb]
        
        for B_items in product(*B_dices):
            B_sums.append(sum(B_items))
        
        B_sums.sort()

        for A_items in product(*A_dices):
            win += bisect_left(B_sums, sum(A_items))
        
        if win > max_win:
            max_win = win
            answer = [x + 1 for x in comb]
                               
    return answer