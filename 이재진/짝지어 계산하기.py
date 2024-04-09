def solution(s):
    answer = -1
    ls = []
    for i in s:
        ls.append(i)
        if len(ls) >= 2 and ls[-1] == ls[-2]:
            for _ in range(2):
                ls.pop()
    
    if len(ls) == 0:
        return 1
    else:
        return 0
