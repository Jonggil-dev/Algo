from itertools import permutations

def solution(ability):
    r = len(ability)
    c = len(ability[0])
    answer = 0
    perms = permutations(range(r), c)
    
    for perm in perms:
        tmp = 0
        for i in range(c):
            tmp += ability[perm[i]][i]
        answer = max(answer, tmp)
    return answer