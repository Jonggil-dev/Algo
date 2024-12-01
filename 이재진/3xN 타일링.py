def solution(n):
    answer = 0
    if n % 2 != 0:
        return 0
    ls = [-1]*5000
    ls[0], ls[1], ls[2], ls[4] = 0, 0, 3, 11
    now = 6
    while now <= n:
        ls[now] = ls[now-2]*4 - ls[now-4]
        now += 2
    return ls[n] % 1000000007
