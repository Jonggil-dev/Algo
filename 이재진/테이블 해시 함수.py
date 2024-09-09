def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x:(x[col-1], -x[0]))
    ls = data[row_begin-1:row_end]
    res = []
    
    for i in range(row_begin, row_end+1):
        d = data[i-1]
        tmp = 0
        for j in d:
            tmp += j%i
        res.append(tmp)
    print(res)
    
    answer = res[0]
    for i in res[1:]:
        answer = answer ^ i
    return answer
