from collections import deque
def val(x):
    dic = {"{": "}", "(":")", "[":"]", "}":-1, ")":-1, "]":-1}
    tmp = []
    for i in x:
        tmp.append(i)
        if len(tmp) >= 2 and tmp[-1] == dic[tmp[-2]]:
            for _ in range(2):
                tmp.pop()
    if len(tmp) == 0:
        return True
    return False

def solution(s):
    answer = 0
    n = len(s)
    ls = list(s)
    for _ in range(n):
        if val(ls):
            answer += 1
        ls.append(ls.pop(0))
    return answer
