from itertools import combinations

def solution(relation):
    keys = set()
    r, c = len(relation), len(relation[0])
    
    for i in range(1, c + 1):
        for comb in combinations(range(c), i):
            candidates = set()
            flag = True
            for re in relation:
                candidates_key = ""
                for co in comb:
                    candidates_key += re[co]
                
                # 유일성 검사
                if candidates_key in candidates:
                    flag = False
                    break
                
                candidates.add(candidates_key)
            
            #최소성 검사
            if flag:
                for key in keys:
                    if set(key).issubset(set(comb)):
                        flag = False
                        break

                if flag:
                    keys.add(comb)
    return len(keys)