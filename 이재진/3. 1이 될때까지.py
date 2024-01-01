for t in range(2):
    N, M = map(int, input().split())
    ls = [sorted(list(map(int, input().split()))) for _ in range(N)]
    res = 0
    for i in ls:
        if i[0] > res:
            res = i[0]
    print(f'#{t}', res)