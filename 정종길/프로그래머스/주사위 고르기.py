from itertools import combinations, product
from bisect import bisect_left


def solution(dice):
    n = len(dice)
    combs = list(combinations(range(n), n // 2))
    max_win = 0

    for comb in combs:
        win = 0
        sum_A = []
        sum_B = []
        A = []

        for A_idx in comb:
            A.append(dice[A_idx])

        B = [dice[B_idx] for B_idx in range(n) if B_idx not in comb]
        for A_pick in product(*A):
            sum_A.append(sum(A_pick))

        for B_pick in product(*B):
            sum_B.append(sum(B_pick))

        sum_A.sort()
        sum_B.sort()

        for A_num in sum_A:
            win += bisect_left(sum_B, A_num)

        if win > max_win:
            max_win = win
            answer = [x + 1 for x in comb]

    return answer
