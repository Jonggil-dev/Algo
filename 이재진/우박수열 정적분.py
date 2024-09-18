def solution(k, ranges):
    answer = []
    ls = [[0,k]]
    num = 1
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        ls.append([num, k])
        num += 1
    
    areas = []
    for i in range(len(ls)-1):
        x1, y1 = ls[i]
        x2, y2 = ls[i+1]
        area = ((abs(x1-x2) * abs(y1-y2))/2) + min(y1,y2)
        areas.append(area)
    
    n = len(ls) - 1
    for a,b in ranges:
        b = n+b
        if a == b:
            answer.append(0)
        elif a > b:
            answer.append(-1)
        else:
            tmp = 0
            for i in range(a,b):
                tmp += areas[i]
            answer.append(tmp)
            
        
        
    return answer
