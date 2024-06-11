def solution(n, k):
    tmp = 0
    tran = ""
    while n > k**tmp:
        tmp += 1
    for i in range(tmp-1,-1,-1):
        t = k**i
        for j in range(k-1,-1,-1):
            if n >= t*j:
                tran += f"{j}"
                n -= t*j
                break
    ls_sub = []
    tmp = 0
    for i in range(len(tran)):
        if tran[i] != "0":
            tmp = tmp*10 + int(tran[i])
        else:
            if tmp != 0:
                ls_sub.append(tmp)
            tmp = 0
    if tmp != 0:
        ls_sub.append(tmp)
    cnt = 0
    for i in ls_sub:
        flag = 1
        if i == 1:
            continue
        elif i == 2:
            cnt += 1
        else:
            for j in range(2, int(i**(1/2))+1):
                if i % j == 0:
                    flag = 0
                    break
            if flag:
                cnt += 1

    return cnt
