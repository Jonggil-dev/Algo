def solution(storey):
    answer = 0
    ls = list(map(int, list(str(storey))))
    tmp = 0
    for i in range(len(ls)-1,-1,-1):
        now = ls[i] + tmp
        if now > 5 or (now == 5 and i > 0 and ls[i-1] >= 5):
            answer += 10-now
            tmp = 1
        else:
            answer += now
            tmp = 0
    if tmp == 1:
        answer += tmp
    return answer
