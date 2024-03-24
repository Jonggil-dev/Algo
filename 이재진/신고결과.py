def solution(id_list, report, k):
    answer = []
    dic = {i:set() for i in id_list}
    for i in report:
        a,b = i.split()
        dic[b].add(a)
    ls = []
    for i in id_list:
        if len(dic[i]) >= k:
            ls.append(i)
    res = {i:set() for i in id_list}
    for i in report:
        a,b = i.split()
        if b in ls:
            res[a].add(b)
    for i in id_list:
        answer.append(len(res[i]))
    return answer
