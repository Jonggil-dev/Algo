from itertools import permutations

def solution(user_id, banned_id):
    answer = set()
    n = len(banned_id)
    
    for pers in permutations(user_id, n):
        flag = True
        for i in range(n):
            if len(pers[i]) != len(banned_id[i]):
                flag = False
                break
                
            if not check(pers[i], banned_id[i]):
                flag = False
                break
                
        if flag:
            answer.add(tuple(sorted(list(pers))))
            
    return len(answer)


def check(user, ban):
    for i in range(len(user)):
        if ban[i] == "*":
            continue
        
        if ban[i] != user[i]:
            return False
        
    return True
        