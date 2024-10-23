from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    global records
    
    answer = []
    records = defaultdict(list)
    
    for data in info:
        l, r, c, f, s = data.split()
        dfs([l, r, c, f], int(s), 0)
    
    for v in records.values():
        v.sort()
        
    for qu in query:
        l, r, c, f, s = qu.replace("and","").split()
        txt = l + r + c + f
        answer.append(len(records[txt]) - bisect_left(records[txt], int(s)))
    return answer

def dfs(li, s, cnt):
    global records
    
    records["".join(li)].append(s)
    
    for i in range(cnt, 4):
        tmp = li[i]
        li[i] = "-"
        dfs(li, s, i + 1)
        li[i] = tmp