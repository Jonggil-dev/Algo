import copy
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    n = len(discount)
    for i in range(n-9):
        tmp = copy.deepcopy(dic)
        for idx in range(i,i+10):
            if discount[idx] not in want or tmp[discount[idx]] == 0:
                break
            tmp[discount[idx]] -= 1
        if sum(tmp.values()) == 0:
            answer += 1
    return answer
