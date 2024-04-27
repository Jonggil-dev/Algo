def solution(n,a,b):
    answer = 1
    while True:
        a = (a+1) // 2
        b = (b+1) // 2
        if a == b:
            break
        answer += 1
    return answer
