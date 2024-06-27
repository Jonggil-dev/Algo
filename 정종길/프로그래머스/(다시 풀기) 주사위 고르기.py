from itertools import combinations, product
from bisect import bisect_left


def solution(dice):
    n = len(dice)
    combs = list(combinations(range(n), n // 2))
    answer_cnt = 0
    answer = []

    for A_comb in combs:
        A = []
        B = []
        sum_A = []
        sum_B = []
        B_comb = []
        cnt = 0

        for i in range(n):
            if i not in A_comb:
                B_comb.append(i)

        for A_dice in A_comb:
            A.append(dice[A_dice])

        for B_dice in B_comb:
            B.append(dice[B_dice])

        for prod in product(*A):
            sum_A.append(sum(prod))

        for prod in product(*B):
            sum_B.append(sum(prod))

        sum_A.sort()
        sum_B.sort()

        for num in sum_A:
            cnt += bisect_left(sum_B, num)

        if cnt > answer_cnt:
            answer_cnt = cnt
            answer = list(A_comb[:])

    for i in range(len(answer)):
        answer[i] += 1

    return answer
