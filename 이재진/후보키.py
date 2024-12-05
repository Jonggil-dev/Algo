from itertools import combinations
def solution(relation):
    answer = 0
    n = len(relation)
    m = len(relation[0])
    ls = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(relation[j][i])
        ls.append(tmp)
    
    k = 1
    dic = {a:[] for a in range(1,m+1)}
    for k in range(m):
        sub = []
        for i in combinations(ls,k):
            tmp = []
            for idx in range(n):
                t = []
                for j in i:
                    t.append(j[idx])
                if t in tmp:
                    break
                else:
                    tmp.append(t)
            if len(tmp) == n:
                sub.append(list(i))
                dic[k].append(list(i))
                
    for key, value in dic.items():
        if key == 1:
            answer += len(value)
            # print(value)
        else:
            for v in value:
                f = True
                for a in range(1,key):
                    flag = 0
                    for b in dic[a]:
                        for c in b:
                            if c in v:
                                flag += 1
                            
                        if flag == a:
                            f = False
                            break
                        flag = 0
                    
                if f:
                    answer += 1
                                
    if answer == 0:
        return 1
    return answer
