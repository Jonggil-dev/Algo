def solution(n):
    answer = ''
    tmp = ''
    while n > 0:
        tmp = str((n%3)) + tmp
        if n%3 == 0:
            n -= 1
        n //= 3
    
    print(tmp)
    for i in tmp:
        if i == '0':
            answer += "4"
        elif i == '1':
            answer += "1"
        elif i == '2':
            answer += "2"
    return answer
