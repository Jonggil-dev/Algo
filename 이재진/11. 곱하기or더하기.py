import sys
T = int(sys.stdin.readline())
for t in range(1, T+1):
    ls = list(map(int, list(sys.stdin.readline().strip())))
    res = 0
    for x in ls:
        if x <= 1 or not res:
            res += x
        else:
            res *= x
    print(f'#{t} {res}')