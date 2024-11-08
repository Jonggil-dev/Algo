from itertools import combinations_with_replacement as com
def solution(n, info):
    answer = []
    num = 0
    arr = []
    for i in com(list(range(11)), n):
        ls = [0] * 11
        for j in i:
            ls[j] += 1
        tmp = cal(info, ls)
        if num < tmp:
            num = tmp
            answer = ls
            arr = []
            arr.append(ls)
        elif num == tmp:
            arr.append(ls)
    
    if len(arr) == 0:
        return [-1]
    elif len(arr) == 1:
        return arr[0]
    else:
        dic = {i:[] for i in range(11)}
        for i in range(11):
            for j in range(len(arr)):
                dic[i].append(arr[j][10-i])
        for i in range(11):
            tmp = dic[i]
            max_num = max(tmp)
            cnt = 0
            idx = -1
            for i in range(len(tmp)):
                if tmp[i] == max_num:
                    cnt += 1
                    idx = i
            if cnt == 1:
                return arr[idx]
        print(dic)
    return answer

def cal(ls1, ls2):
    a, b = 0, 0
    n = len(ls1)
    for i in range(n):
        if ls1[i] != 0 or ls2[i] != 0:
            if ls1[i] >= ls2[i]:
                a += 10-i
            else:
                b += 10-i
    if a < b:
        return b-a
    else:
        return -1
    
