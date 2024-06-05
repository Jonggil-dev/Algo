import copy
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    dic1 = dict()
    dic2 = dict()
    for i in range(len(str1)-1):
        a = str1[i]
        b = str1[i+1]
        if a.isalpha() and b.isalpha():
            if f"{a}{b}" in dic1:
                dic1[f"{a}{b}"] += 1
            else:
                dic1[f"{a}{b}"] = 1
    for i in range(len(str2)-1):
        a = str2[i]
        b = str2[i+1]
        if a.isalpha() and b.isalpha():
            if f"{a}{b}" in dic2:
                dic2[f"{a}{b}"] += 1
            else:
                dic2[f"{a}{b}"] = 1
    inter = 0
    for i in dic1.keys():
        if i in dic2.keys():
            inter += min(dic1[i], dic2[i])
    for i in dic2.keys():
        if i in dic1.keys():
            dic1[i] = max(dic1[i], dic2[i])
        else:
            dic1[i] = dic2[i]
    uni = sum(dic1.values())
    if uni == 0:
        return 65536
    tmp = inter / uni
    answer = int(tmp * 65536)
    return answer
