def solution(friends, gifts):
    import copy
    ls = [[0]*len(friends) for _ in range(len(friends))]
    dic = {i:[0, 0, 0] for i in friends}
    for g in gifts:
        i, j = g.split(' ')
        # 선물 표
        ni, nj = friends.index(i), friends.index(j)
        ls[ni][nj] += 1
        
        # 선물 지수
        dic[i][0] += 1
        dic[j][1] += 1
    for f in friends:
        dic[f][2] = dic[f][0] - dic[f][1]
    res_ls = [0]*len(friends)
    for ni in range(len(friends)):
        for nj in range(len(friends)):
            if ni == nj:
                pass
            # ni, nj = friends.index(friends[i]), friends.index(friends[j])
            if ls[ni][nj] > ls[nj][ni]:
                res_ls[ni] += 1
            elif ls[ni][nj] < ls[nj][ni]:
                res_ls[nj] += 1
            elif ls[ni][nj] == ls[nj][ni]:
                if dic[friends[ni]][2] > dic[friends[nj]][2]:
                    res_ls[ni] += 1
                elif dic[friends[ni]][2] < dic[friends[nj]][2]:
                    res_ls[nj] += 1
    print(ls)
    print(dic)
    answer = max(res_ls) // 2
    return answer



# 준 선물 / 받은 선물 / 선물 지수
