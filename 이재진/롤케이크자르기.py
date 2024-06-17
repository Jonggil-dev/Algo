def solution(topping):
    answer = 0
    a = dict()
    b = dict()
    for i in topping:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    for i in topping:
        if len(a.keys()) == len(b.keys()):
            answer += 1
        if a[i] == 1:
            del a[i]
        else:
            a[i] -= 1
        
        if i in b:
            b[i] += 1
        else:
            b[i] = 1

    return answer
