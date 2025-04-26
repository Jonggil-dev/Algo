'''
1. 엄청 복잡하게 풀었음
2. 2회차 풀이가 훨씬 간단함
'''

import sys
sys.setrecursionlimit(100000)

def solution(enroll, referral, seller, amount):
    global enroll_idxs, graph, answer, sell_info
    enroll_idxs = { name : idx for idx, name in enumerate(enroll) }
    enroll_idxs["-"] = len(enroll)
    sell_info = {}
    graph = [[] for _ in range(len(enroll) + 1)]
    answer = [[] for _ in range(len(enroll) + 1)]
    
    
    for i in range(len(referral)):
        parent, son = enroll_idxs[referral[i]], enroll[i]
        graph[parent].append(son)        

    for idx, s in enumerate(seller):
        if s not in sell_info:
            sell_info[s] = [amount[idx] * 100]
        else:
            sell_info[s].append(amount[idx] * 100)

    dfs("-")
    answer.pop()
    for i in range(len(answer)):
        answer[i] = sum(answer[i])
        
    return answer

def dfs(now):
    global enroll_idxs, graph, answer, sell_info
    
    if now in sell_info:
        e_idx = enroll_idxs[now]
        for pay in sell_info[now]:
            answer[e_idx].append(pay)
    
    now = enroll_idxs[now]
    for son in graph[now]:
        dfs(son)
        son_idx = enroll_idxs[son]
        for i in range(len(answer[son_idx])):
            pay = answer[son_idx][i]
            devide = pay // 10
            if devide != 0:
                answer[now].append(devide)
            remain = pay - devide
            answer[son_idx][i] = remain