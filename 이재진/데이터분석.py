def solution(data, ext, val_ext, sort_by):
    dic = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    answer = []
    for d in data:
        if d[dic[ext]] < val_ext:
            answer.append(d)
    answer = sorted(answer, key = lambda x:x[dic[sort_by]])
    return answer
