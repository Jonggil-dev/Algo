def solution(n, left, right):
    answer = []
    ls = list(range(1, n+1))
    for i in range(left+1, right+2):
        a = i // n
        b = i % n
        if b==0:
            answer.append(ls[-1])
        elif a < b:
            answer.append(ls[b-1])
        else:
            answer.append(ls[a])
    return answer
