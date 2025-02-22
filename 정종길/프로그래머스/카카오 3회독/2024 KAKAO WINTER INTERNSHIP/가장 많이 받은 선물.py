def solution(friends, gifts):
    answer = 0
    n = len(friends)
    
    idxs = { name : idx for idx, name in enumerate(friends)}
    give_to = [[0] * n for _ in range(n)]
    matrics = [[0] * 3 for _ in range(n)]
    
    for info in gifts:
        give, take = info.split()
        gidx, tidx = idxs[give], idxs[take]
        give_to[gidx][tidx] += 1
        matrics[gidx][0] += 1
        matrics[gidx][2] += 1
        matrics[tidx][1] += 1
        matrics[tidx][2] -= 1
        
    for g in range(n):
        next_month = 0
        for t in range(n):
            if g == t:
                continue
            
            if give_to[g][t] > give_to[t][g]:
                next_month += 1
                
            elif give_to[g][t] == give_to[t][g]:
                if matrics[g][2] > matrics[t][2]:
                    next_month += 1
        answer = max(answer, next_month)
        
    return answer