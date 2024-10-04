from itertools import permutations

def solution(user_id, banned_id):
    answer = []

    for per in permutations(user_id, len(banned_id)):
        flag = False
        for user_id, ban_id in zip(per, banned_id):
            if not check_ban(ban_id, user_id):
                flag = True
                break
                
        if not flag:
            if set(per) not in answer:
                answer.append(set(per))
    
    return len(answer)


def check_ban(ban, user):
    if len(ban) == len(user):
        for i in range(len(user)):
            if ban[i] == "*":
                continue
            if ban[i] != user[i]:
                return False
        return True
    return False
