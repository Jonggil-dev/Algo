from collections import defaultdict
import bisect
from itertools import combinations
def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for i in info:
        tmp = i.split()
        con = tmp[:-1]
        score = int(tmp[-1])

        for j in range(5):
            for com in combinations(list(range(4)),j):
                tmp_con = con[:]
                for idx in com:
                    tmp_con[idx] = "-"
                key = "".join(tmp_con)
                dic[key].append(score)

    for k in dic.keys():
        dic[k].sort()

    for q in query:
        tmp = q.replace(" and ", " ").split()
        con = tmp[:-1]
        score = int(tmp[-1])
        key = "".join(con)

        scores = dic[key]
        idx = bisect.bisect_left(scores, score)
        answer.append(len(scores) - idx)

    return answer
