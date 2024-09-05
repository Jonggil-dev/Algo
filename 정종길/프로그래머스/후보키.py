from itertools import combinations

def solution(relation):
    answer = 0
    N = len(relation[0])
    keys = []
    for i in range(1, N + 1):
        combs = combinations(range(N), i)
        for comb in combs:
            if check_valid(comb, keys):
                tmp = []
                for rel in relation:
                    word = ""
                    for idx in comb:
                        word += rel[idx]
                    tmp.append(word)

                if len(set(tmp)) == len(tmp):
                    keys.append(comb)
                    answer += 1
    return answer

def check_valid(comb, keys):
    for key in keys:
        if set(key).issubset(comb):   
            return False
    return True