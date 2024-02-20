def solution(name, yearning, photo):
    answer = []
    for i in photo:
        res = 0
        for j in i:
            if j in name:
                res += yearning[name.index(j)]
        answer.append(res)
    return answer
