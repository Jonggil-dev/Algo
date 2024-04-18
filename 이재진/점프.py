def solution(n):
    res = 0
    while True:
        if n == 1:
            res += 1
            break
        if n % 2 == 0:
            n //= 2
        else:
            res += 1
            n -= 1
            n //= 2
    return res
