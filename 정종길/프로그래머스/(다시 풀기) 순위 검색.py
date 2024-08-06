from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    global dict_
    answer = []
    dict_ = defaultdict(list)
    
    for text in info:
        li = text.split()
        dfs(-1, li)
    
    for v in dict_.values():
        v.sort()
    
    for qu in query:
        qu = qu.replace("and", " ")
        l, p, c, f, s= qu.split()
        answer.append(len(dict_[l + p + c + f]) - bisect_left(dict_[l + p + c + f], int(s)))
        
    return answer

def dfs(i, li):
    l, p, c, f, s = li
    dict_[l + p + c + f].append(int(s))
    
    for j in range(i + 1, 4):
        original = li[j]
        li[j] = "-"
        dfs(j, li)
        li[j] = original