import math
def solution(w,h):
    answer = w*h
    tmp = 0
    k = 0
    if w < h:
        for x in range(1,w+1):
            y = (x*h)/w
            tmp += math.ceil(y)-math.floor(k)
            k = y
            if x!=0 and y%1 == 0:
                break
        answer -= (w//x)*tmp
    else:
        for x in range(1,h+1):
            y = (x*w)/h
            tmp += math.ceil(y)-math.floor(k)
            k = y
            if x!=0 and y%1 == 0:
                break
        answer -= (h//x)*tmp
    return answer

