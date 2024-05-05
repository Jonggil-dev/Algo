def solution(n,a,b):
    answer = 0

    while (a != b):
        a = next_round(a)
        b = next_round(b)
        answer += 1

    return answer

def next_round(num):
    if num % 2 == 0:
        return num // 2
    else:
        return (num + 1) // 2