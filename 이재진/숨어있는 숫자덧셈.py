def solution(my_string):
    answer = 0
    tmp = ''
    for i in my_string:
        if i.isnumeric():
            tmp += i
        else:
            if tmp != '':
                answer += int(tmp)
                tmp = ''
    if tmp != '':
        answer += int(tmp)
    return answer
