def solution(k, tangerine):
    answer = 0
    dic = dict()
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    ls = sorted(list(dic.values()), reverse = True)
    for i in ls:
        answer += 1
        if k <= i:
            return answer
        else:
            k -= i
    return answer
