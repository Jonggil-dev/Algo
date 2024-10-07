def solution(friends, gifts):
    answer = 0
    idxs = { name : i for i, name in enumerate(friends)}
    n = len(friends)
    
    tables = [[0] * n for _ in range(n)]
    give_matrics = {}
    receive_matrics = {}
    
    for gift in gifts:
        give, receive = gift.split()
        gi, ri = idxs[give], idxs[receive]
        tables[gi][ri] += 1
        give_matrics[idxs[give]] = give_matrics.get(idxs[give], 0) + 1
        receive_matrics[idxs[receive]] = receive_matrics.get(idxs[receive], 0) + 1
    
    for i in range(n):
        cnt = 0
        give_matric = give_matrics.get(i, 0) - receive_matrics.get(i, 0)
        
        for j in range(n):
            if i == j:
                continue
            
            if tables[i][j] > tables[j][i]:
                cnt += 1
                continue
            
            if tables[i][j] == tables[j][i]:
                receive_matric = give_matrics.get(j, 0) - receive_matrics.get(j, 0)
                if give_matric > receive_matric:
                    cnt += 1

        answer = max(cnt, answer)
    return answer