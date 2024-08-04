from itertools import combinations

def solution(orders, course):
    dict_ = {}
    answer = []
    for order in orders:
        order = ''.join(sorted(list(order)))
        for cour in course:
            for comb in combinations(order, cour):
                comb = ''.join(comb)
                dict_[comb] = dict_.get(comb, 0) + 1
    for cour in course:
        tmp = []
        max_v = 2
        for key, value in dict_.items():
            if len(key) == cour:
                if value > max_v:
                    max_v = value
                    tmp = [key]
                elif value == max_v:
                    tmp.append(key)
        answer.extend(tmp)
    
    return sorted(answer)