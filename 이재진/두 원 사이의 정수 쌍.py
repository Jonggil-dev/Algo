def solution(r1, r2):
    answer = 0
    tmp1, tmp2 = 0,0
    cnt = 0
    for i in range(-r2, r2+1):
        tmp = (r2**2 - i**2)**(0.5)
        tmp2 += int(tmp)*2 + 1
    for i in range(-r1, r1+1):
        tmp = (r1**2 - i**2)**(0.5)
        if tmp % 1 == 0:
            if tmp == 0:
                cnt += 1
            else:
                cnt += 2
        tmp1 += int(tmp)*2 + 1
    print(tmp1, tmp2)
    answer = tmp2 - tmp1 + cnt
    return answer
