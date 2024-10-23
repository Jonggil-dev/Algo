from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    global records;
    
    records = defaultdict(list)
    answer = []
    
    for data in info:
        make_records(-1, data.split())
    
    for v in records.values():
        v.sort()
        
    for que in query:
        que = que.replace("and", " ")
        a, b, c, d, score = que.split()
        answer.append(len(records[a + b + c + d]) - bisect_left(records[a + b + c + d], int(score)))
        
    return answer

def make_records(i, li):
    global records
    
    a, b, c, d, score = li
    records[a + b + c + d].append(int(score))
    
    for j in range(i + 1, 4):
        origin = li[j]
        li[j] = "-"
        make_records(j, li)
        li[j] = origin